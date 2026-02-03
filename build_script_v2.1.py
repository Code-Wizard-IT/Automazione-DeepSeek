import os

prompt_dir = r"C:\Users\cresc\Desktop\Prompt"
output_file = r"C:\Users\cresc\Desktop\figma-deepseek-automation-v2.1.user.js"

# Read all 12 prompt files
prompts = []
for i in range(1, 13):
    fname_prefix = f"PROMPT-FIGMA-{i:02d}-"
    for f in os.listdir(prompt_dir):
        if f.startswith(fname_prefix) and f.endswith('.md'):
            fpath = os.path.join(prompt_dir, f)
            with open(fpath, 'r', encoding='utf-8') as fp:
                content = fp.read()
            short_name = f.replace('PROMPT-FIGMA-', '').replace('.md', '')
            prompts.append({'id': i, 'name': short_name, 'content': content})
            break

print(f"Loaded {len(prompts)} prompts")

def escape_js_template(text):
    text = text.replace('\\', '\\\\')
    text = text.replace('`', '\\`')
    text = text.replace('${', '\\${')
    return text

# Build prompt array JS code
prompt_array_items = []
for p in prompts:
    marker_instruction = (
        "\n\n---\n\n"
        "**ISTRUZIONE FINALE OBBLIGATORIA:**\n"
        "Quando hai completato TUTTE le sezioni richieste, "
        "scrivi ESATTAMENTE questa stringa su una NUOVA RIGA alla fine della tua risposta:\n"
        f"===PROMPT_{p['id']}_COMPLETATO===\n\n"
        "NON scrivere questa stringa prima di aver completato TUTTO il contenuto richiesto."
    )
    full_content = p['content'] + marker_instruction
    escaped = escape_js_template(full_content)
    item = f"    {{\n      id: {p['id']},\n      name: \"FIGMA-{p['name']}\",\n      content: `{escaped}`\n    }}"
    prompt_array_items.append(item)

prompts_js = "  const PROMPTS = [\n" + ",\n".join(prompt_array_items) + "\n  ];\n"

script_parts = []

# ═══════════════════════════════════════════
# PART 1: METADATA + CONFIG
# ═══════════════════════════════════════════
script_parts.append("""// ==UserScript==
// @name         Figma DeepSeek Automation v2.1
// @namespace    http://tampermonkey.net/
// @version      2.1
// @description  Automazione 12 prompt Figma su DeepSeek — Triple-Lock + anti-detection + salvataggio diretto
// @author       AutoGen
// @match        https://chat.deepseek.com/*
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
  'use strict';

  // ═══════════════════════════════════════════
  // §1. CONFIG
  // ═══════════════════════════════════════════
  const CONFIG = {
    TYPING_DELAY: 50,
    POLL_INTERVAL: 3000,
    MAX_POLL_CYCLES: 200,
    STALE_THRESHOLD: 5,
    MARKER_PREFIX: '===PROMPT_',
    MARKER_SUFFIX: '_COMPLETATO===',
    NEW_CHAT_URL: 'https://chat.deepseek.com/',
    TRIPLE_LOCK_INTERVAL: 2000,
    TRIPLE_LOCK_REQUIRED: 5,
    TRIPLE_LOCK_TAIL_CHARS: 500,
    STORAGE_PREFIX: 'figma2_',
    CONTINUE_MAX_RETRIES: 15,
    WAIT_FOR_RESPONSE_MAX: 30,
    WAIT_FOR_RESPONSE_INTERVAL: 2000,
    MIN_PART_SIZE: 100,             // minimum chars to save as a part

    // Anti-detection: Jitter & Pacing
    TYPING_DELAY_MIN: 30,            // ms min typing delay
    TYPING_DELAY_MAX: 90,            // ms max typing delay
    INTER_PROMPT_PAUSE_MIN: 10000,   // 10s min between prompts
    INTER_PROMPT_PAUSE_MAX: 30000,   // 30s max between prompts
    LONG_BREAK_EVERY: 8,             // long break every N prompts
    LONG_BREAK_MIN: 180000,          // 3 min min break
    LONG_BREAK_MAX: 300000,          // 5 min max break

    // Error recovery
    RATE_LIMIT_WAIT: 60000,          // 1 min wait on "too frequently"
    SERVER_BUSY_WAIT: 30000,         // 30s wait on "server busy"
    ERROR_MAX_RETRIES: 10,           // max retries per error type
  };
""")

# ═══════════════════════════════════════════
# PART 2: PROMPTS
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §2. PROMPTS (12 Figma Graphic Design)
  // ═══════════════════════════════════════════
""")
script_parts.append(prompts_js)

# ═══════════════════════════════════════════
# PART 3: STATE
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §3. STATE
  // ═══════════════════════════════════════════
  const STATE = {
    running: false,
    nextPromptId: 1,
    executionId: 0,
    totalExported: 0,
    totalParts: 0,
    log: [],
    folderReady: false,
  };
""")

# ═══════════════════════════════════════════
# PART 4: PERSISTENCE
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §4. PERSISTENCE (localStorage)
  // ═══════════════════════════════════════════
  function saveState() {
    try {
      localStorage.setItem(CONFIG.STORAGE_PREFIX + 'state', JSON.stringify({
        running: STATE.running,
        nextPromptId: STATE.nextPromptId,
        totalExported: STATE.totalExported,
        totalParts: STATE.totalParts,
      }));
    } catch(e) { console.error('[FIGMA] saveState error', e); }
  }

  function loadState() {
    try {
      const raw = localStorage.getItem(CONFIG.STORAGE_PREFIX + 'state');
      if (raw) return JSON.parse(raw);
    } catch(e) { console.error('[FIGMA] loadState error', e); }
    return null;
  }

  function clearPersistedState() {
    const keys = [];
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k && k.startsWith(CONFIG.STORAGE_PREFIX)) keys.push(k);
    }
    keys.forEach(k => localStorage.removeItem(k));
    log('\\u{1F5D1} Cache cleared');
  }

  function cacheFullExport(promptId, text) {
    try {
      localStorage.setItem(CONFIG.STORAGE_PREFIX + 'export_' + promptId, text);
    } catch(e) { console.error('[FIGMA] cacheExport error', e); }
  }

  function getCachedExport(promptId) {
    return localStorage.getItem(CONFIG.STORAGE_PREFIX + 'export_' + promptId);
  }
""")

print("Parts 1-4 done")

# ═══════════════════════════════════════════
# PART 5: FILE SYSTEM ACCESS API (NEW)
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §5. FILE SYSTEM ACCESS API
  // ═══════════════════════════════════════════
  let rootDirHandle = null;

  // ─── IndexedDB for handle persistence ───
  function openIDB() {
    return new Promise((resolve, reject) => {
      const req = indexedDB.open('figma-auto-db', 1);
      req.onupgradeneeded = () => req.result.createObjectStore('handles');
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
  }

  async function saveHandleToIDB(handle) {
    try {
      const db = await openIDB();
      const tx = db.transaction('handles', 'readwrite');
      tx.objectStore('handles').put(handle, 'rootDir');
    } catch(e) { console.error('[FIGMA] saveHandleToIDB error', e); }
  }

  async function loadHandleFromIDB() {
    try {
      const db = await openIDB();
      return new Promise((resolve) => {
        const tx = db.transaction('handles', 'readonly');
        const req = tx.objectStore('handles').get('rootDir');
        req.onsuccess = () => resolve(req.result || null);
        req.onerror = () => resolve(null);
      });
    } catch(e) { return null; }
  }

  // ─── Request folder access (needs user gesture) ───
  async function requestFolderAccess() {
    try {
      rootDirHandle = await window.showDirectoryPicker({
        id: 'figma-deepseek-output',
        mode: 'readwrite',
        startIn: 'desktop',
      });
      await saveHandleToIDB(rootDirHandle);
      STATE.folderReady = true;
      log('\\u{1F4C1} Folder access granted: ' + rootDirHandle.name);
      updateUI();
      return true;
    } catch(e) {
      log('\\u{26A0} Folder access denied or cancelled: ' + e.message);
      STATE.folderReady = false;
      updateUI();
      return false;
    }
  }

  // ─── Try to restore handle from IndexedDB ───
  async function tryRestoreFolder() {
    const handle = await loadHandleFromIDB();
    if (!handle) return false;
    try {
      const perm = await handle.queryPermission({ mode: 'readwrite' });
      if (perm === 'granted') {
        rootDirHandle = handle;
        STATE.folderReady = true;
        log('\\u{1F4C1} Folder restored: ' + handle.name);
        updateUI();
        return true;
      }
      // Need user gesture to re-request — we'll prompt via UI button
      return false;
    } catch(e) { return false; }
  }

  // ─── Re-grant permission (after browser restart, needs user gesture) ───
  async function reGrantPermission() {
    const handle = await loadHandleFromIDB();
    if (!handle) return requestFolderAccess();
    try {
      const perm = await handle.requestPermission({ mode: 'readwrite' });
      if (perm === 'granted') {
        rootDirHandle = handle;
        STATE.folderReady = true;
        log('\\u{1F4C1} Folder permission re-granted: ' + handle.name);
        updateUI();
        return true;
      }
    } catch(e) {}
    return requestFolderAccess();
  }

  // ─── Save a part file to the filesystem ───
  async function savePartToFilesystem(promptObj, partNumber, text) {
    const folderName = padNum(promptObj.id) + '-' + promptObj.name;
    const fileName = promptObj.name + '-parte-' + partNumber + '.txt';

    const header = [
      '\\u{2550}'.repeat(60),
      'FIGMA CATALOG: ' + promptObj.name,
      'Prompt ID: ' + promptObj.id + ' / ' + PROMPTS.length,
      'Parte: ' + partNumber,
      'Exported: ' + new Date().toISOString(),
      'Characters: ' + text.length,
      '\\u{2550}'.repeat(60),
      '',
      '',
    ].join('\\n');
    const fullContent = header + text;

    // Try File System Access API
    if (rootDirHandle) {
      try {
        const subDir = await rootDirHandle.getDirectoryHandle(folderName, { create: true });
        const fileHandle = await subDir.getFileHandle(fileName, { create: true });
        const writable = await fileHandle.createWritable();
        await writable.write(fullContent);
        await writable.close();
        log('\\u{1F4BE} Saved: ' + folderName + '/' + fileName + ' (' + text.length + ' chars)');
        STATE.totalParts++;
        return true;
      } catch(e) {
        log('\\u{26A0} Filesystem write failed: ' + e.message + ' — falling back to download');
      }
    }

    // Fallback: browser download
    downloadTextFile(folderName + '--' + fileName, fullContent);
    STATE.totalParts++;
    return false;
  }
""")

print("Part 5 (File System Access API) done")

# ═══════════════════════════════════════════
# PART 6: UTILITY
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §6. UTILITY
  // ═══════════════════════════════════════════
  function log(msg) {
    const ts = new Date().toLocaleTimeString('it-IT');
    const entry = '[' + ts + '] ' + msg;
    STATE.log.push(entry);
    if (STATE.log.length > 500) STATE.log.shift();
    console.log('[FIGMA] ' + entry);
    updateUI();
  }

  function sleep(ms) {
    return new Promise(r => setTimeout(r, ms));
  }

  function padNum(n, len = 2) {
    return String(n).padStart(len, '0');
  }

  function randomBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
""")

# ═══════════════════════════════════════════
# PART 7: DOM HELPERS
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §7. DOM HELPERS
  // ═══════════════════════════════════════════
  function getTextarea() {
    return document.querySelector('textarea#chat-input') ||
           document.querySelector('textarea[placeholder]') ||
           document.querySelector('textarea');
  }

  function getAllResponses() {
    // Primary: exact class "ds-markdown" (response containers, not paragraphs)
    // Excludes ds-markdown-paragraph, ds-markdown-html which are child elements
    const primary = document.querySelectorAll('.ds-markdown');
    if (primary.length > 0) {
      // Filter: only elements whose class is exactly "ds-markdown" (no sub-variants)
      const filtered = Array.from(primary).filter(function(el) {
        return !el.classList.contains('ds-markdown-paragraph') &&
               !el.classList.contains('ds-markdown-html');
      });
      if (filtered.length > 0) return filtered;
    }
    // Fallback selectors for other chat platforms
    const fallbacks = [
      '[class*="markdown"]',
      '.assistant-message',
      '.response-content',
    ];
    for (const sel of fallbacks) {
      const els = document.querySelectorAll(sel);
      if (els.length > 0) return Array.from(els);
    }
    return [];
  }

  function countResponses() {
    return getAllResponses().length;
  }

  function collectAllResponseText() {
    return getAllResponses().map(el => el.innerText || el.textContent || '').join('\\n\\n---\\n\\n');
  }

  function getLastResponseText() {
    const all = getAllResponses();
    if (all.length === 0) return '';
    const last = all[all.length - 1];
    return last.innerText || last.textContent || '';
  }

  function scrollToBottom() {
    try {
      const containers = document.querySelectorAll('[class*="conversation"], [class*="chat"], main');
      containers.forEach(c => { c.scrollTop = c.scrollHeight; });
      window.scrollTo(0, document.body.scrollHeight);
    } catch(e) {}
  }
""")

# ═══════════════════════════════════════════
# PART 8: GENERATION DETECTION
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §8. GENERATION & LIMIT DETECTION
  // ═══════════════════════════════════════════
  function isStillGenerating() {
    const panel = document.getElementById('figma-auto-panel');
    const stopBtns = document.querySelectorAll('button, div[role="button"]');
    for (const btn of stopBtns) {
      if (panel && panel.contains(btn)) continue; // skip our own UI buttons
      const txt = (btn.textContent || '').toLowerCase().trim();
      const ariaLabel = (btn.getAttribute('aria-label') || '').toLowerCase();
      if (txt.includes('stop') || ariaLabel.includes('stop')) return true;
    }
    const loadingIndicators = document.querySelectorAll(
      '[class*="loading"], [class*="typing"], [class*="generating"], .ds-loading'
    );
    for (const el of loadingIndicators) {
      if (el.offsetParent !== null) return true;
    }
    const cursors = document.querySelectorAll('[class*="cursor"], [class*="caret"]');
    for (const c of cursors) {
      const style = window.getComputedStyle(c);
      if (style.animationName && style.animationName !== 'none') return true;
    }
    return false;
  }

  function detectMaxLengthReached() {
    const allText = document.body.innerText || '';
    const patterns = [
      'lunghezza massima raggiunta',
      'maximum length reached',
      'max length reached',
      'output limit',
      'token limit',
    ];
    const lower = allText.toLowerCase();
    return patterns.some(p => lower.includes(p));
  }

  function findContinueButton() {
    const btns = document.querySelectorAll('button, div[role="button"], a');
    for (const btn of btns) {
      const txt = (btn.textContent || '').toLowerCase().trim();
      if (
        txt.includes('continue generating') ||
        txt.includes('continua a generare') ||
        (txt.includes('continue') && txt.length < 30)
      ) {
        return btn;
      }
    }
    return null;
  }

  function detectRateLimit() {
    const allText = (document.body.innerText || '').toLowerCase();
    const patterns = [
      'sending messages too frequently',
      'too many requests',
      'rate limit',
      'troppi messaggi',
      'messaggi troppo frequenti',
    ];
    return patterns.some(function(p) { return allText.includes(p); });
  }

  function detectServerBusy() {
    const allText = (document.body.innerText || '').toLowerCase();
    const patterns = [
      'server is busy',
      'please try again later',
      'server busy',
      'il server \\u{00E8} occupato',
      '\\u{670D}\\u{52A1}\\u{5668}\\u{7E41}\\u{5FD9}',
    ];
    return patterns.some(function(p) { return allText.includes(p); });
  }

  async function handleErrorWithRetry(errorType, retryCount) {
    const waitTime = errorType === 'rate_limit'
      ? CONFIG.RATE_LIMIT_WAIT
      : CONFIG.SERVER_BUSY_WAIT;
    const jitter = randomBetween(0, 15000);
    const totalWait = waitTime + jitter;
    log('\\u{26A0} ' + errorType.toUpperCase() + ' detected (retry ' + retryCount + '/' + CONFIG.ERROR_MAX_RETRIES + ')');
    log('\\u{23F3} Waiting ' + Math.round(totalWait / 1000) + 's before retry...');
    await sleep(totalWait);
    // Try dismissing error dialogs/toasts
    const dismissBtns = document.querySelectorAll('button, div[role="button"]');
    for (const btn of dismissBtns) {
      const txt = (btn.textContent || '').toLowerCase().trim();
      if (txt.includes('try again') || txt.includes('retry') || txt.includes('riprova') ||
          txt.includes('regenerate') || txt.includes('rigenera') || txt === 'ok') {
        btn.click();
        await sleep(2000);
        break;
      }
    }
  }
""")

print("Parts 6-8 done")

# ═══════════════════════════════════════════
# PART 9: NEW CHAT NAVIGATION
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §9. NEW CHAT NAVIGATION
  // ═══════════════════════════════════════════
  async function navigateToNewChat() {
    log('\\u{1F195} Navigating to new chat...');

    // Strategy 1: "+" icon button in top-left area (rightmost ds-icon-button = new chat)
    try {
      const iconBtns = Array.from(document.querySelectorAll('div.ds-icon-button, button.ds-icon-button'));
      const topBtns = iconBtns.filter(function(btn) {
        const rect = btn.getBoundingClientRect();
        return rect.top < 80 && rect.left < 300 && btn.querySelector('svg');
      });
      if (topBtns.length >= 2) {
        // Sort by x position — rightmost is the "+" new chat button
        topBtns.sort(function(a, b) { return a.getBoundingClientRect().left - b.getBoundingClientRect().left; });
        const btn = topBtns[topBtns.length - 1];
        log('  Strategy 1: Found "+" new chat button (rightmost of ' + topBtns.length + ' icons)');
        btn.click();
        await sleep(2000);
        return true;
      }
    } catch(e) {}

    // Strategy 2: "new chat" text link/button
    try {
      const clickables = document.querySelectorAll('a, button, div[role="button"], span[role="button"]');
      for (const el of clickables) {
        const txt = (el.textContent || '').toLowerCase();
        const aria = (el.getAttribute('aria-label') || '').toLowerCase();
        const href = (el.getAttribute('href') || '').toLowerCase();
        if (
          txt.includes('new chat') || txt.includes('nuova chat') ||
          aria.includes('new chat') || href === '/'
        ) {
          log('  Strategy 2: Found text/link button');
          el.click();
          await sleep(2000);
          return true;
        }
      }
    } catch(e) {}

    // Strategy 3: URL navigation (full reload)
    log('  Strategy 3: URL navigation (reload)');
    saveState();
    window.location.replace(CONFIG.NEW_CHAT_URL + '?_t=' + Date.now());
    return true;
  }
""")

# ═══════════════════════════════════════════
# PART 10: FILE DOWNLOAD (fallback)
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §10. FILE DOWNLOAD (fallback for non-filesystem)
  // ═══════════════════════════════════════════
  function downloadTextFile(filename, content) {
    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    log('\\u{1F4BE} Downloaded: ' + filename);
  }

  async function downloadAllAsZip() {
    log('\\u{1F4E6} Creating ZIP...');
    if (typeof JSZip === 'undefined') {
      const script = document.createElement('script');
      script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
      document.head.appendChild(script);
      await new Promise((resolve, reject) => {
        script.onload = resolve;
        script.onerror = reject;
      });
      await sleep(500);
    }
    const zip = new JSZip();
    let count = 0;
    for (const p of PROMPTS) {
      const cached = getCachedExport(p.id);
      if (cached) {
        const folder = zip.folder(padNum(p.id) + '-' + p.name);
        folder.file('FIGMA-' + padNum(p.id) + '-' + p.name + '-FULL.txt', cached);
        count++;
      }
    }
    if (count === 0) {
      log('\\u{26A0} No cached exports found for ZIP');
      return;
    }
    const blob = await zip.generateAsync({ type: 'blob' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'figma-catalogs-' + new Date().toISOString().slice(0,10) + '.zip';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    log('\\u{1F4E6} ZIP downloaded with ' + count + ' files');
  }
""")

# ═══════════════════════════════════════════
# PART 11: SEND MESSAGE
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §11. SEND MESSAGE
  // ═══════════════════════════════════════════
  async function typeAndSend(text) {
    const textarea = getTextarea();
    if (!textarea) throw new Error('Textarea not found');

    const nativeSetter = Object.getOwnPropertyDescriptor(
      window.HTMLTextAreaElement.prototype, 'value'
    ).set;
    nativeSetter.call(textarea, text);
    textarea.dispatchEvent(new Event('input', { bubbles: true }));
    textarea.dispatchEvent(new Event('change', { bubbles: true }));
    await sleep(randomBetween(CONFIG.TYPING_DELAY_MIN, CONFIG.TYPING_DELAY_MAX));

    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
    await sleep(300);

    const sendSelectors = [
      'button[aria-label*="send" i]',
      'button[aria-label*="invia" i]',
      'div[role="button"][aria-label*="send" i]',
      'button.ds-button--primary',
    ];
    let sendBtn = null;
    for (const sel of sendSelectors) {
      sendBtn = document.querySelector(sel);
      if (sendBtn && !sendBtn.disabled) break;
      sendBtn = null;
    }
    if (!sendBtn) {
      const allBtns = document.querySelectorAll('button:not([disabled])');
      for (const btn of allBtns) {
        if (btn.querySelector('svg') && btn.closest('form, [class*="input"], [class*="chat"]')) {
          sendBtn = btn;
          break;
        }
      }
    }
    if (sendBtn) {
      sendBtn.click();
      log('\\u{1F4E4} Message sent');
    } else {
      textarea.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));
      log('\\u{1F4E4} Message sent via Enter key');
    }
    await sleep(1000);
  }

  async function sendContinueAsText() {
    log('\\u{1F4DD} Sending "Continua" as text...');
    await typeAndSend('Continua');
  }
""")

# ═══════════════════════════════════════════
# PART 12: WAIT UNTIL READY
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §12. WAIT UNTIL READY
  // ═══════════════════════════════════════════
  async function waitUntilReady(maxWait = 60000) {
    const start = Date.now();
    let diagCount = 0;
    while (Date.now() - start < maxWait) {
      const ta = getTextarea();
      const generating = isStillGenerating();
      if (ta && !ta.disabled && !generating) return true;
      diagCount++;
      if (diagCount % 5 === 0) {
        const elapsed = Math.round((Date.now() - start) / 1000);
        log('\\u{23F3} waitUntilReady: ' + elapsed + 's | textarea=' + !!ta + ' disabled=' + (ta ? ta.disabled : 'N/A') + ' generating=' + generating);
      }
      await sleep(2000);
    }
    log('\\u{26A0} waitUntilReady timeout after ' + Math.round(maxWait/1000) + 's');
    return false;
  }
""")

print("Parts 9-12 done")

# ═══════════════════════════════════════════
# PART 13: EXECUTE SINGLE PROMPT (TRIPLE-LOCK + PARTS)
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §13. EXECUTE SINGLE PROMPT — TRIPLE-LOCK + PARTS
  // ═══════════════════════════════════════════
  //
  // FLOW:
  // 1. Send prompt → wait for response
  // 2. Poll loop:
  //    - If Triple-Lock confirms → export FINAL part → done
  //    - If "Continue generating" button appears →
  //        export current part → click Continue → keep polling
  //    - If text goes stale (no marker) →
  //        export current part → send "Continua" → keep polling
  //    - If timeout → export remaining as final part
  //
  // Each "part" = text generated since last export point.
  // Files: parte-1.txt, parte-2.txt, ...
  //
  async function executePrompt(promptObj, currentExecId) {
    const marker = CONFIG.MARKER_PREFIX + promptObj.id + CONFIG.MARKER_SUFFIX;
    let partNumber = 0;
    let lastExportedPos = 0;
    let lastTextLength = 0;
    let staleCount = 0;
    let continueRetries = 0;
    let tripleLockCount = 0;

    log('\\u{1F3AF} Starting prompt ' + promptObj.id + ': ' + promptObj.name);

    // Wait for textarea ready
    const ready = await waitUntilReady();
    if (!ready) {
      log('\\u{274C} Textarea not ready, aborting prompt');
      return 'error';
    }
    if (currentExecId !== STATE.executionId) return 'cancelled';

    // Count existing responses (baseline)
    const baselineCount = countResponses();
    log('\\u{1F4CA} Baseline responses: ' + baselineCount);

    // Send the prompt
    await typeAndSend(promptObj.content);
    if (currentExecId !== STATE.executionId) return 'cancelled';

    // Wait for new response to appear
    let newResponseDetected = false;
    for (let w = 0; w < CONFIG.WAIT_FOR_RESPONSE_MAX; w++) {
      if (currentExecId !== STATE.executionId) return 'cancelled';
      if (countResponses() > baselineCount) {
        newResponseDetected = true;
        log('\\u{2705} New response detected');
        break;
      }
      await sleep(CONFIG.WAIT_FOR_RESPONSE_INTERVAL);
    }
    if (!newResponseDetected) {
      log('\\u{26A0} No new response appeared after waiting');
      return 'error';
    }

    // ─── MAIN POLLING LOOP ───
    for (let cycle = 0; cycle < CONFIG.MAX_POLL_CYCLES; cycle++) {
      if (currentExecId !== STATE.executionId) return 'cancelled';

      scrollToBottom();
      const fullText = getLastResponseText();
      const currentLength = fullText.length;

      // ─── 1. TRIPLE-LOCK CONFIRMATION ───
      const markerFound = fullText.includes(marker);
      const markerInTail = markerFound && fullText.slice(-CONFIG.TRIPLE_LOCK_TAIL_CHARS).includes(marker);
      const generationStopped = !isStillGenerating();

      if (markerFound && markerInTail && generationStopped) {
        tripleLockCount++;
        log('\\u{1F512} Triple-Lock ' + tripleLockCount + '/' + CONFIG.TRIPLE_LOCK_REQUIRED + ' PASSED');

        if (tripleLockCount >= CONFIG.TRIPLE_LOCK_REQUIRED) {
          log('\\u{2705}\\u{2705}\\u{2705} TRIPLE-LOCK CONFIRMED for prompt ' + promptObj.id);
          // Export final part
          partNumber++;
          const partText = fullText.substring(lastExportedPos);
          if (partText.length > CONFIG.MIN_PART_SIZE) {
            await savePartToFilesystem(promptObj, partNumber, partText);
          }
          cacheFullExport(promptObj.id, fullText);
          STATE.totalExported++;
          return 'completed';
        }

        await sleep(CONFIG.TRIPLE_LOCK_INTERVAL);
        continue;
      } else {
        if (tripleLockCount > 0) {
          const reasons = [];
          if (!markerFound) reasons.push('marker not found');
          else if (!markerInTail) reasons.push('marker not in tail');
          if (!generationStopped) reasons.push('still generating');
          log('\\u{26A0} Triple-Lock RESET at ' + tripleLockCount + '/' + CONFIG.TRIPLE_LOCK_REQUIRED + ' (' + reasons.join(', ') + ')');
        }
        tripleLockCount = 0;
      }

      // ─── 2. CONTINUE GENERATING BUTTON ───
      const continueBtn = findContinueButton();
      if (continueBtn && !isStillGenerating() && continueRetries < CONFIG.CONTINUE_MAX_RETRIES) {
        // Generation paused with continue button → EXPORT CURRENT PART first
        partNumber++;
        const partText = fullText.substring(lastExportedPos);
        if (partText.length > CONFIG.MIN_PART_SIZE) {
          log('\\u{1F4BE} Exporting parte ' + partNumber + ' before Continue (' + partText.length + ' chars)');
          await savePartToFilesystem(promptObj, partNumber, partText);
          lastExportedPos = currentLength;
        } else {
          partNumber--; // revert if too small
        }

        continueRetries++;
        log('\\u{1F504} Clicking "Continue" (' + continueRetries + '/' + CONFIG.CONTINUE_MAX_RETRIES + ')');
        continueBtn.click();
        staleCount = 0;
        await sleep(CONFIG.POLL_INTERVAL);
        continue;
      }

      // ─── 3. MAX LENGTH DETECTION ───
      if (detectMaxLengthReached() && !isStillGenerating() && !continueBtn) {
        // Truly stuck at max length with no continue option
        partNumber++;
        const partText = fullText.substring(lastExportedPos);
        if (partText.length > CONFIG.MIN_PART_SIZE) {
          log('\\u{26A0} Max length reached — exporting parte ' + partNumber);
          await savePartToFilesystem(promptObj, partNumber, partText);
        }
        cacheFullExport(promptObj.id, fullText);
        STATE.totalExported++;
        return 'max_length_done';
      }

      // ─── 4. STALE DETECTION ───
      if (currentLength === lastTextLength && currentLength > 0 && !isStillGenerating()) {
        staleCount++;
        if (staleCount >= CONFIG.STALE_THRESHOLD) {
          if (!markerFound && continueRetries < CONFIG.CONTINUE_MAX_RETRIES) {
            // Text stopped growing, no marker → export part + send "Continua"
            partNumber++;
            const partText = fullText.substring(lastExportedPos);
            if (partText.length > CONFIG.MIN_PART_SIZE) {
              log('\\u{1F4BE} Exporting parte ' + partNumber + ' before Continua (' + partText.length + ' chars)');
              await savePartToFilesystem(promptObj, partNumber, partText);
              lastExportedPos = currentLength;
            } else {
              partNumber--;
            }

            continueRetries++;
            log('\\u{1F504} Stale content \\u{2014} sending "Continua" (attempt ' + continueRetries + ')');
            await sendContinueAsText();
            staleCount = 0;
          } else {
            // Max retries reached OR marker was found but Triple-Lock didn't pass
            log('\\u{26A0} Stale after max retries \\u{2014} accepting as done');
            partNumber++;
            const partText = fullText.substring(lastExportedPos);
            if (partText.length > CONFIG.MIN_PART_SIZE) {
              await savePartToFilesystem(promptObj, partNumber, partText);
            }
            cacheFullExport(promptObj.id, fullText);
            STATE.totalExported++;
            return 'stale_completed';
          }
        }
      } else {
        staleCount = 0;
      }
      lastTextLength = currentLength;

      // ─── PROGRESS LOG ───
      if (cycle > 0 && cycle % 10 === 0) {
        log('\\u{1F4CA} Cycle ' + cycle + '/' + CONFIG.MAX_POLL_CYCLES +
            ' | ' + currentLength + ' chars | parts:' + partNumber +
            ' | stale:' + staleCount + ' | lock:' + tripleLockCount);
      }

      await sleep(CONFIG.POLL_INTERVAL);
    }

    // ─── TIMEOUT ───
    const finalText = getLastResponseText();
    if (finalText.length > lastExportedPos + CONFIG.MIN_PART_SIZE) {
      partNumber++;
      log('\\u{23F0} Timeout \\u{2014} exporting remaining as parte ' + partNumber);
      await savePartToFilesystem(promptObj, partNumber, finalText.substring(lastExportedPos));
      cacheFullExport(promptObj.id, finalText);
      STATE.totalExported++;
      return 'timeout_exported';
    }
    log('\\u{274C} Timeout with no substantial content');
    return 'timeout_empty';
  }
""")

print("Part 13 (executePrompt with Triple-Lock + Parts) done")

# ═══════════════════════════════════════════
# PART 14: RUN ALL (with folder access)
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §14. RUN ALL (Orchestrator)
  // ═══════════════════════════════════════════
  async function runAll(startFrom = 1) {
    if (STATE.running) {
      log('\\u{26A0} Already running \\u{2014} click Stop first to reset');
      return;
    }

    // Ensure folder access before starting
    if (!rootDirHandle) {
      log('\\u{1F4C1} Requesting output folder access...');
      const granted = await requestFolderAccess();
      if (!granted) {
        log('\\u{274C} Cannot start without folder access. Select a folder first.');
        return;
      }
    }

    STATE.running = true;
    STATE.executionId++;
    STATE.nextPromptId = startFrom;
    const currentExecId = STATE.executionId;
    log('\\u{1F680} Starting automation from prompt ' + startFrom + '/' + PROMPTS.length);
    log('\\u{1F6E1} Anti-detection: jitter ON, periodic breaks every ' + CONFIG.LONG_BREAK_EVERY + ' prompts');
    saveState();
    updateUI();

    try {
      for (let i = startFrom - 1; i < PROMPTS.length; i++) {
        if (currentExecId !== STATE.executionId) {
          log('\\u{1F6D1} Execution cancelled');
          break;
        }

        const promptObj = PROMPTS[i];
        STATE.nextPromptId = promptObj.id;
        saveState();
        updateUI();

        log('');
        log('\\u{2550}'.repeat(40));
        log('\\u{1F4CB} Prompt ' + promptObj.id + '/' + PROMPTS.length + ': ' + promptObj.name);
        log('\\u{2550}'.repeat(40));

        let result;
        let errorRetries = 0;

        // ── Pre-flight: check for rate limit / server busy ──
        while (errorRetries < CONFIG.ERROR_MAX_RETRIES) {
          if (currentExecId !== STATE.executionId) break;
          if (detectRateLimit()) {
            await handleErrorWithRetry('rate_limit', ++errorRetries);
            continue;
          }
          if (detectServerBusy()) {
            await handleErrorWithRetry('server_busy', ++errorRetries);
            continue;
          }
          break;
        }

        try {
          result = await executePrompt(promptObj, currentExecId);
        } catch (promptErr) {
          log('\\u{274C} executePrompt ERROR: ' + promptErr.message);
          console.error('[FIGMA] executePrompt error:', promptErr);
          result = 'error';
        }

        // ── Post-prompt: check for errors and retry if needed ──
        if (result === 'error' && errorRetries < CONFIG.ERROR_MAX_RETRIES) {
          if (detectRateLimit() || detectServerBusy()) {
            const errType = detectRateLimit() ? 'rate_limit' : 'server_busy';
            await handleErrorWithRetry(errType, ++errorRetries);
            log('\\u{1F504} Retrying prompt ' + promptObj.id + ' after error recovery...');
            await navigateToNewChat();
            await sleep(5000);
            await waitUntilReady(30000);
            i--;
            continue;
          }
        }
        log('Result: ' + result);

        if (currentExecId !== STATE.executionId) break;

        // Handle result \\u{2014} retry on max_length like v1
        if (result === 'max_length_done') {
          log('\\u{1F504} Max length \\u{2014} retrying same prompt in new chat...');
          STATE.nextPromptId = promptObj.id;
          saveState();
          await navigateToNewChat();
          await sleep(3000);
          await waitUntilReady();
          i--;
          continue;
        }

        // Move to next prompt
        STATE.nextPromptId = promptObj.id + 1;
        saveState();

        // If not the last prompt, navigate to new chat
        if (i < PROMPTS.length - 1) {
          // ── Periodic long break (anti-detection) ──
          const promptsDone = promptObj.id - startFrom + 1;
          if (promptsDone > 0 && promptsDone % CONFIG.LONG_BREAK_EVERY === 0) {
            const breakTime = randomBetween(CONFIG.LONG_BREAK_MIN, CONFIG.LONG_BREAK_MAX);
            log('\\u{2615} Long break: ' + Math.round(breakTime / 60000) + ' min (after ' + promptsDone + ' prompts)');
            updateUI();
            await sleep(breakTime);
          }

          // ── Random inter-prompt pause ──
          const pauseTime = randomBetween(CONFIG.INTER_PROMPT_PAUSE_MIN, CONFIG.INTER_PROMPT_PAUSE_MAX);
          log('\\u{23F1} Pause: ' + Math.round(pauseTime / 1000) + 's before next prompt');
          await sleep(pauseTime);

          log('\\u{1F195} Opening new chat for next prompt...');
          await navigateToNewChat();
          await sleep(3000);
          const ready = await waitUntilReady(30000);
          if (!ready) {
            log('\\u{26A0} New chat not ready, forcing reload...');
            saveState();
            window.location.replace(CONFIG.NEW_CHAT_URL + '?_t=' + Date.now());
            return; // auto-resume will continue
          }
        }
      }
    } catch (fatalErr) {
      log('\\u{1F4A5} FATAL ERROR in runAll: ' + fatalErr.message);
      console.error('[FIGMA] FATAL runAll error:', fatalErr);
    } finally {
      // ALWAYS reset running state so user can restart
      if (currentExecId === STATE.executionId) {
        STATE.running = false;
        saveState();
        updateUI();
      }
    }

    // Summary
    if (currentExecId === STATE.executionId) {
      log('');
      if (STATE.nextPromptId > PROMPTS.length) {
        log('\\u{1F389} ALL ' + PROMPTS.length + ' PROMPTS COMPLETED!');
      } else {
        log('\\u{26A0} Stopped at prompt ' + STATE.nextPromptId);
      }
      log('\\u{1F4BE} Total parts saved: ' + STATE.totalParts);
      log('\\u{1F6E1} Anti-detection was active throughout');
      log('\\u{1F4E6} Use "Export ZIP" for full cached responses');
    }
  }
""")

# ═══════════════════════════════════════════
# PART 15: AUTO-RESUME
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §15. AUTO-RESUME
  // ═══════════════════════════════════════════
  async function checkAutoResume() {
    const saved = loadState();
    if (!saved || !saved.running) return;
    if (saved.nextPromptId > PROMPTS.length) {
      log('\\u{2705} All prompts were already completed');
      clearPersistedState();
      return;
    }
    log('\\u{1F504} AUTO-RESUME detected: continuing from prompt ' + saved.nextPromptId);
    STATE.totalExported = saved.totalExported || 0;
    STATE.totalParts = saved.totalParts || 0;

    // Try to restore folder handle
    const restored = await tryRestoreFolder();
    if (!restored) {
      log('\\u{26A0} Folder access lost after reload \\u{2014} click "\\u{1F4C1} Folder" to re-grant');
      // Show a notification but don't block — user can click the button
      // We'll wait a few seconds and then try reGrant which needs user gesture
      // For now, set a flag so the UI shows prominently
      STATE.folderReady = false;
      updateUI();

      // Wait for user to click the folder button (poll every 2s for 30s max)
      for (let w = 0; w < 15; w++) {
        if (rootDirHandle) break;
        await sleep(2000);
      }
      if (!rootDirHandle) {
        log('\\u{26A0} No folder access \\u{2014} outputs will download to browser default');
      }
    }

    await sleep(3000);
    await waitUntilReady(30000);
    runAll(saved.nextPromptId);
  }
""")

print("Parts 14-15 done")

# ═══════════════════════════════════════════
# PART 16: UI (with folder button)
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §16. UI (Floating Panel)
  // ═══════════════════════════════════════════
  let uiPanel = null;
  let uiStatus = null;
  let uiProgressBar = null;
  let uiFolderIndicator = null;

  function createUI() {
    uiPanel = document.createElement('div');
    uiPanel.id = 'figma-auto-panel';
    uiPanel.innerHTML = `
      <div id="figma-auto-header" style="cursor:move;padding:8px 12px;background:#4F46E5;color:#FFF;font-weight:700;font-size:13px;border-radius:8px 8px 0 0;display:flex;justify-content:space-between;align-items:center;">
        <span>\\u{1F3A8} Figma Auto v2.1</span>
        <span style="font-size:11px;opacity:0.7">${PROMPTS.length} prompts</span>
      </div>
      <div style="padding:10px 12px;">
        <div id="figma-auto-folder" style="font-size:11px;padding:4px 8px;margin-bottom:6px;border-radius:4px;background:#FEF3C7;color:#92400E;cursor:pointer;text-align:center;" title="Click to select output folder">
          \\u{1F4C1} No folder selected
        </div>
        <div id="figma-auto-status" style="font-size:11px;color:#666;margin-bottom:8px;min-height:28px;line-height:1.4;">Ready</div>
        <div style="background:#E5E7EB;border-radius:4px;height:6px;margin-bottom:10px;overflow:hidden;">
          <div id="figma-auto-progress" style="background:#4F46E5;height:100%;width:0%;transition:width 0.5s;border-radius:4px;"></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">
          <button id="figma-btn-start" style="grid-column:1/3;padding:8px;background:#4F46E5;color:#FFF;border:none;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;">\\u{25B6} Start All</button>
          <button id="figma-btn-stop" style="padding:6px;background:#EF4444;color:#FFF;border:none;border-radius:6px;font-size:11px;cursor:pointer;">\\u{23F9} Stop</button>
          <button id="figma-btn-from" style="padding:6px;background:#F59E0B;color:#FFF;border:none;border-radius:6px;font-size:11px;cursor:pointer;">\\u{1F4CD} Start From #</button>
          <button id="figma-btn-zip" style="padding:6px;background:#10B981;color:#FFF;border:none;border-radius:6px;font-size:11px;cursor:pointer;">\\u{1F4E6} ZIP</button>
          <button id="figma-btn-clear" style="padding:6px;background:#6B7280;color:#FFF;border:none;border-radius:6px;font-size:11px;cursor:pointer;">\\u{1F5D1} Clear</button>
        </div>
      </div>
    `;
    Object.assign(uiPanel.style, {
      position: 'fixed', bottom: '10px', left: '10px', width: '240px',
      background: '#FFF', borderRadius: '8px', boxShadow: '0 4px 24px rgba(0,0,0,0.15)',
      zIndex: '999999', fontFamily: 'system-ui, -apple-system, sans-serif',
      border: '1px solid #E5E7EB',
    });
    document.body.appendChild(uiPanel);

    uiStatus = document.getElementById('figma-auto-status');
    uiProgressBar = document.getElementById('figma-auto-progress');
    uiFolderIndicator = document.getElementById('figma-auto-folder');

    // Folder indicator click → select/change folder
    uiFolderIndicator.addEventListener('click', async () => {
      if (rootDirHandle) {
        // Already have folder — offer to change
        const change = confirm('Current folder: ' + rootDirHandle.name + '\\nChange output folder?');
        if (!change) return;
      }
      // Try reGrant first (if handle exists in IDB), else new picker
      await reGrantPermission();
    });

    // Dragging
    const header = document.getElementById('figma-auto-header');
    let isDragging = false, dragX = 0, dragY = 0;
    header.addEventListener('mousedown', (e) => {
      isDragging = true;
      dragX = e.clientX - uiPanel.offsetLeft;
      dragY = e.clientY - uiPanel.offsetTop;
    });
    document.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      uiPanel.style.left = (e.clientX - dragX) + 'px';
      uiPanel.style.right = 'auto';
      uiPanel.style.top = (e.clientY - dragY) + 'px';
      uiPanel.style.bottom = 'auto';
    });
    document.addEventListener('mouseup', () => { isDragging = false; });

    // Button handlers
    document.getElementById('figma-btn-start').addEventListener('click', () => runAll(1));
    document.getElementById('figma-btn-stop').addEventListener('click', () => {
      STATE.executionId++;
      STATE.running = false;
      clearPersistedState();
      log('\\u{1F6D1} Stopped by user');
      updateUI();
    });
    document.getElementById('figma-btn-from').addEventListener('click', () => {
      const num = prompt('Start from prompt # (1-' + PROMPTS.length + '):');
      const n = parseInt(num);
      if (n >= 1 && n <= PROMPTS.length) runAll(n);
      else if (num !== null) alert('Enter a number between 1 and ' + PROMPTS.length);
    });
    document.getElementById('figma-btn-zip').addEventListener('click', () => downloadAllAsZip());
    document.getElementById('figma-btn-clear').addEventListener('click', () => {
      if (confirm('Clear all cached exports?')) clearPersistedState();
    });
  }

  function updateUI() {
    if (!uiStatus) return;
    const lastLog = STATE.log.length > 0 ? STATE.log[STATE.log.length - 1] : 'Ready';
    uiStatus.textContent = lastLog.replace(/^\\[.*?\\]\\s*/, '');
    if (uiProgressBar) {
      const pct = STATE.running
        ? ((STATE.nextPromptId - 1) / PROMPTS.length * 100)
        : (STATE.totalExported / PROMPTS.length * 100);
      uiProgressBar.style.width = Math.min(pct, 100) + '%';
    }
    if (uiFolderIndicator) {
      if (rootDirHandle && STATE.folderReady) {
        uiFolderIndicator.style.background = '#D1FAE5';
        uiFolderIndicator.style.color = '#065F46';
        uiFolderIndicator.textContent = '\\u{1F4C1} ' + rootDirHandle.name + ' \\u{2705}';
      } else {
        uiFolderIndicator.style.background = '#FEF3C7';
        uiFolderIndicator.style.color = '#92400E';
        uiFolderIndicator.textContent = '\\u{1F4C1} Click to select output folder';
      }
    }
  }
""")

print("Part 16 (UI) done")

# ═══════════════════════════════════════════
# PART 17: CONSOLE API
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §17. CONSOLE API
  // ═══════════════════════════════════════════
  window.FIGMA_AUTO = {
    start: (from = 1) => runAll(from),
    stop: () => {
      STATE.executionId++;
      STATE.running = false;
      clearPersistedState();
      log('\\u{1F6D1} Stopped via console');
    },
    status: () => ({
      running: STATE.running,
      nextPromptId: STATE.nextPromptId,
      totalExported: STATE.totalExported,
      totalParts: STATE.totalParts,
      totalPrompts: PROMPTS.length,
      folderReady: STATE.folderReady,
      folderName: rootDirHandle ? rootDirHandle.name : null,
      log: STATE.log.slice(-20),
    }),
    zip: () => downloadAllAsZip(),
    clearCache: () => clearPersistedState(),
    selectFolder: () => requestFolderAccess(),
  };
""")

# ═══════════════════════════════════════════
# PART 18: INIT
# ═══════════════════════════════════════════
script_parts.append("""
  // ═══════════════════════════════════════════
  // §18. INIT
  // ═══════════════════════════════════════════
  setTimeout(async () => {
    createUI();
    log('\\u{1F3A8} Figma DeepSeek Automation v2.1 loaded');
    log('\\u{1F4CB} ' + PROMPTS.length + ' prompts | Triple-Lock | Anti-detection');
    log('\\u{1F6E1} Jitter: ' + CONFIG.TYPING_DELAY_MIN + '-' + CONFIG.TYPING_DELAY_MAX + 'ms | Breaks every ' + CONFIG.LONG_BREAK_EVERY + ' prompts');

    // Try to restore folder access from IndexedDB
    const restored = await tryRestoreFolder();
    if (restored) {
      log('\\u{1F4C1} Output folder: ' + rootDirHandle.name);
    } else {
      log('\\u{1F4C1} Click the folder indicator to select output folder');
    }

    // Check auto-resume
    checkAutoResume();
  }, 2000);

})();
""")

# ═══════════════════════════════════════════
# FINAL: ASSEMBLE AND SAVE
# ═══════════════════════════════════════════
full_script = ''.join(script_parts)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(full_script)

# Verification
total_lines = full_script.count('\n')
total_chars = len(full_script)
marker_count = full_script.count('===PROMPT_') - 1  # minus the one in CONFIG
has_triple_lock = 'tripleLockCount' in full_script
has_filesystem = 'showDirectoryPicker' in full_script
has_parts = 'lastExportedPos' in full_script
has_save_part = 'savePartToFilesystem' in full_script

print(f"\n{'='*60}")
print(f"Script saved to: {output_file}")
print(f"Total size: {total_chars:,} characters")
print(f"Total lines: {total_lines:,}")
print(f"Prompt markers: {marker_count}")
print(f"Triple-Lock: {'YES' if has_triple_lock else 'NO'}")
print(f"File System API: {'YES' if has_filesystem else 'NO'}")
print(f"Parts tracking: {'YES' if has_parts else 'NO'}")
print(f"savePartToFilesystem: {'YES' if has_save_part else 'NO'}")
print(f"{'='*60}")
print("Done!")
