#!/usr/bin/env python3
"""
DeepSeek Full Automation v3 - Secure Edition
CDP injection + local file server + auto-shutdown + security hardening

Security features:
- Auth token on file server (random per-session)
- Path traversal protection
- CORS restricted to DeepSeek origin
- CDP origin restricted
- Max request size limit
- Auto-shutdown on completion
"""

import asyncio
import json
import os
import secrets
import signal
import subprocess
import sys
import threading
import time
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ═══════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════

CDP_PORT = 9222
CDP_URL = f"http://localhost:{CDP_PORT}/json"
SCRIPT_PATH = r"C:\Users\cresc\Desktop\figma-deepseek-automation-v2.1.user.js"
DEEPSEEK_URL = "chat.deepseek.com"
CHROME_USER_DATA = r"C:\Users\cresc\ChromeCDP"
CDP_TIMEOUT = 30
OUTPUT_PATH = r"C:\Users\cresc\Desktop\output deepseek\new"
FILE_SERVER_PORT = 8765
MAX_REQUEST_SIZE = 5 * 1024 * 1024  # 5MB max per request
AUTO_SHUTDOWN_TIMEOUT = 4 * 3600    # 4 hours max runtime safety
MONITOR_INTERVAL = 30               # check status every 30s
ALLOWED_ORIGIN = f"https://{DEEPSEEK_URL}"

# Per-session random auth token
AUTH_TOKEN = secrets.token_hex(32)

# Start prompt (override via command line: python start_full_automation.py 3)
START_FROM = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# ═══════════════════════════════════════════════════════════
# SECURE FILE SERVER
# ═══════════════════════════════════════════════════════════

def is_safe_path(component):
    """Validate path component against traversal attacks"""
    if not component:
        return True
    dangerous = ['..', '/', '\\', '\x00', '~']
    for d in dangerous:
        if d in component:
            return False
    if os.path.isabs(component):
        return False
    return True


class SecureFileWriteHandler(BaseHTTPRequestHandler):
    """Handles POST requests with auth token and path validation"""

    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', ALLOWED_ORIGIN)
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Auth-Token')
        self.send_header('Vary', 'Origin')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        # Reject all GET requests
        self.send_response(405)
        self.end_headers()

    def do_POST(self):
        # 1. Verify auth token
        token = self.headers.get('X-Auth-Token', '')
        if token != AUTH_TOKEN:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'{"error":"unauthorized"}')
            print(f"  [BLOCKED] Unauthorized request from {self.client_address}")
            return

        # 2. Check request size
        length = int(self.headers.get('Content-Length', 0))
        if length > MAX_REQUEST_SIZE:
            self.send_response(413)
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error":"too large"}')
            print(f"  [BLOCKED] Request too large: {length:,} bytes")
            return

        try:
            data = json.loads(self.rfile.read(length))
            folder = data.get('folder', '')
            filename = data.get('filename', '')
            content = data.get('content', '')

            # 3. Path traversal protection
            if not is_safe_path(folder) or not is_safe_path(filename):
                self.send_response(400)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"error":"invalid path"}')
                print(f"  [BLOCKED] Path traversal attempt: {folder}/{filename}")
                return

            if not filename:
                self.send_response(400)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"error":"no filename"}')
                return

            # 4. Build safe path
            if folder:
                target_dir = os.path.join(OUTPUT_PATH, folder)
            else:
                target_dir = OUTPUT_PATH

            # 5. Verify resolved path is inside OUTPUT_PATH
            resolved = os.path.realpath(target_dir)
            if not resolved.startswith(os.path.realpath(OUTPUT_PATH)):
                self.send_response(403)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"error":"path escape"}')
                print(f"  [BLOCKED] Path escape: {resolved}")
                return

            os.makedirs(target_dir, exist_ok=True)
            filepath = os.path.join(target_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            size = len(content.encode('utf-8'))
            print(f"  [FILE] {filepath} ({size:,} bytes)")

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True}).encode())

        except Exception as e:
            print(f"  [ERROR] {e}")
            self.send_response(500)
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False}).encode())

    def log_message(self, format, *args):
        pass


def start_file_server():
    server = HTTPServer(('127.0.0.1', FILE_SERVER_PORT), SecureFileWriteHandler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server

# ═══════════════════════════════════════════════════════════
# CDP HELPERS
# ═══════════════════════════════════════════════════════════

def check_cdp():
    try:
        with urllib.request.urlopen(CDP_URL, timeout=2) as r:
            return r.status == 200
    except:
        return False


def launch_chrome():
    try:
        result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq chrome.exe'],
                                capture_output=True, text=True, timeout=5)
        if 'chrome.exe' in result.stdout:
            print("  Closing existing Chrome...")
            subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], capture_output=True, timeout=10)
            time.sleep(3)
    except:
        pass

    print("  Launching Chrome with CDP + anti-throttle...")
    subprocess.Popen([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        f'--remote-debugging-port={CDP_PORT}',
        f'--remote-allow-origins=http://127.0.0.1:{FILE_SERVER_PORT}',
        f'--user-data-dir={CHROME_USER_DATA}',
        '--no-first-run',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-renderer-backgrounding',
        f'https://{DEEPSEEK_URL}'
    ])


def shutdown_chrome():
    """Kill Chrome CDP cleanly"""
    print("  Shutting down Chrome CDP...")
    try:
        # Try graceful close via CDP
        urllib.request.urlopen(f"http://localhost:{CDP_PORT}/json/close", timeout=2)
    except:
        pass
    try:
        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'],
                      capture_output=True, timeout=10)
    except:
        pass


def wait_for_cdp(timeout=CDP_TIMEOUT):
    print(f"  Waiting for CDP (timeout: {timeout}s)...")
    start = time.time()
    while time.time() - start < timeout:
        if check_cdp():
            return True
        time.sleep(0.5)
    return False


def get_tabs():
    try:
        with urllib.request.urlopen(CDP_URL, timeout=5) as r:
            return json.loads(r.read().decode())
    except:
        return []


def find_deepseek_tab(tabs):
    for t in tabs:
        if t.get("type") == "page" and DEEPSEEK_URL in t.get("url", ""):
            return t
    return None


def read_script():
    try:
        with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"  Error reading script: {e}")
        return None

# ═══════════════════════════════════════════════════════════
# MOCK JS (with auth token + anti-throttle)
# ═══════════════════════════════════════════════════════════

def build_mock_js():
    return """
(function() {
    // ─── Anti-throttle: fake Page Visibility API ───
    Object.defineProperty(document, 'hidden', { get: () => false, configurable: true });
    Object.defineProperty(document, 'visibilityState', { get: () => 'visible', configurable: true });
    document.addEventListener('visibilitychange', function(e) { e.stopImmediatePropagation(); }, true);
    const origRAF = window.requestAnimationFrame;
    window.requestAnimationFrame = function(cb) {
        return origRAF ? origRAF.call(window, cb) : setTimeout(cb, 16);
    };
    console.log('[AntiThrottle] Visibility mock active');

    // ─── Mock File System API with auth ───
    const SERVER = 'http://127.0.0.1:__PORT__/save';
    const TOKEN = '__TOKEN__';

    class MockWritableStream {
        constructor(folder, filename) {
            this._folder = folder;
            this._filename = filename;
            this._chunks = [];
        }
        async write(data) {
            if (typeof data === 'string') {
                this._chunks.push(data);
            } else if (data instanceof Blob) {
                this._chunks.push(await data.text());
            } else if (data && data.type === 'write') {
                const d = data.data;
                this._chunks.push(typeof d === 'string' ? d : await d.text());
            } else if (data instanceof ArrayBuffer) {
                this._chunks.push(new TextDecoder().decode(data));
            } else if (data instanceof Uint8Array) {
                this._chunks.push(new TextDecoder().decode(data));
            }
        }
        async close() {
            const content = this._chunks.join('');
            try {
                const resp = await fetch(SERVER, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Auth-Token': TOKEN
                    },
                    body: JSON.stringify({
                        folder: this._folder,
                        filename: this._filename,
                        content: content
                    })
                });
                if (!resp.ok) console.error('[MockFS] Write failed:', this._filename, resp.status);
            } catch(e) {
                console.error('[MockFS] Server error:', e);
            }
        }
        async abort() { this._chunks = []; }
    }

    class MockFileHandle {
        constructor(folder, name) {
            this.kind = 'file';
            this.name = name;
            this._folder = folder;
        }
        async createWritable(opts) {
            return new MockWritableStream(this._folder, this.name);
        }
        async getFile() { return new File([], this.name); }
        async requestPermission(opts) { return 'granted'; }
        async queryPermission(opts) { return 'granted'; }
    }

    class MockDirectoryHandle {
        constructor(name, parentPath) {
            this.kind = 'directory';
            this.name = name;
            this._parentPath = parentPath || '';
        }
        get _fullPath() {
            return this._parentPath ? this._parentPath + '/' + this.name : this.name;
        }
        async getDirectoryHandle(name, opts) {
            return new MockDirectoryHandle(name, this._fullPath);
        }
        async getFileHandle(name, opts) {
            return new MockFileHandle(this._fullPath, name);
        }
        async removeEntry(name, opts) { return undefined; }
        async resolve(possibleDescendant) { return null; }
        async requestPermission(opts) { return 'granted'; }
        async queryPermission(opts) { return 'granted'; }
        async *entries() {}
        async *keys() {}
        async *values() {}
        [Symbol.asyncIterator]() { return this.entries(); }
    }

    window.showDirectoryPicker = async function(opts) {
        console.log('[MockFS] Directory picker intercepted');
        return new MockDirectoryHandle('', '');
    };

    console.log('[MockFS] Secure mock installed (token-auth active)');
    return true;
})();
""".replace('__PORT__', str(FILE_SERVER_PORT)).replace('__TOKEN__', AUTH_TOKEN)

# ═══════════════════════════════════════════════════════════
# STATUS MONITOR + AUTO-SHUTDOWN
# ═══════════════════════════════════════════════════════════

async def monitor_until_complete(ws_url):
    """Monitor automation status and auto-shutdown when done"""
    import websockets

    start_time = time.time()
    last_prompt = 0

    while True:
        elapsed = time.time() - start_time

        # Safety timeout
        if elapsed > AUTO_SHUTDOWN_TIMEOUT:
            print(f"\n  [TIMEOUT] Max runtime ({AUTO_SHUTDOWN_TIMEOUT//3600}h) reached. Shutting down...")
            return 'timeout'

        try:
            async with websockets.connect(ws_url, max_size=None) as ws:
                await ws.send(json.dumps({
                    "id": 99, "method": "Runtime.evaluate",
                    "params": {"expression": "FIGMA_AUTO.status()", "returnByValue": True}
                }))
                resp = json.loads(await ws.recv())
                val = resp.get("result", {}).get("result", {}).get("value", "")
                status = json.loads(val) if isinstance(val, str) else val

                running = status.get('running', False)
                current = status.get('nextPromptId', 0)
                total = status.get('totalPrompts', 0)
                exported = status.get('totalExported', 0)

                # Progress update
                if current != last_prompt:
                    mins = int(elapsed // 60)
                    print(f"  [{mins}m] Prompt {current}/{total} | Exported: {exported}")
                    last_prompt = current

                # Check completion
                if not running and exported > 0:
                    print(f"\n  Automation finished! {exported} files exported in {int(elapsed//60)}m")
                    return 'complete'

        except Exception as e:
            # CDP connection lost = Chrome crashed or closed
            print(f"\n  [WARNING] CDP connection lost: {e}")
            return 'disconnected'

        await asyncio.sleep(MONITOR_INTERVAL)

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

async def run():
    import websockets

    print("=" * 60)
    print("  DeepSeek Full Automation v3 - Secure Edition")
    print("=" * 60)
    print(f"  Start from prompt: {START_FROM}")
    print(f"  Output: {OUTPUT_PATH}")
    print(f"  Auth token: {AUTH_TOKEN[:8]}...{AUTH_TOKEN[-8:]}")
    print()

    # Step 1: File server
    print("[1/7] Starting secure file server...")
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    server = start_file_server()
    print(f"  Listening on 127.0.0.1:{FILE_SERVER_PORT} (localhost only)")
    print(f"  Auth: token-protected | CORS: {ALLOWED_ORIGIN}")
    print(f"  Path validation: active | Max size: {MAX_REQUEST_SIZE//1024//1024}MB")
    print()

    # Step 2: CDP
    print("[2/7] Connecting to Chrome CDP...")
    if not check_cdp():
        launch_chrome()
        if not wait_for_cdp():
            print("FAILED: Chrome CDP did not start")
            return 1
    else:
        print("  CDP already running")
    print()

    await asyncio.sleep(1)

    # Step 3: Find tab
    print("[3/7] Finding DeepSeek tab...")
    tabs = get_tabs()
    tab = find_deepseek_tab(tabs)
    if not tab:
        print("  No DeepSeek tab, opening...")
        url = f"http://localhost:{CDP_PORT}/json/new?https://{DEEPSEEK_URL}"
        with urllib.request.urlopen(url, timeout=10) as r:
            json.loads(r.read().decode())
        await asyncio.sleep(5)
        tabs = get_tabs()
        tab = find_deepseek_tab(tabs)
        if not tab:
            print("FAILED: Cannot find DeepSeek tab")
            return 1
    print(f"  Tab: {tab.get('title', 'Unknown')}")
    ws_url = tab["webSocketDebuggerUrl"]
    print()

    # Step 4: Inject main script
    print("[4/7] Injecting automation script...")
    script = read_script()
    if not script:
        return 1
    print(f"  Script: {len(script):,} bytes")

    async with websockets.connect(ws_url, max_size=None) as ws:
        # Cleanup
        await ws.send(json.dumps({
            "id": 1, "method": "Runtime.evaluate",
            "params": {"expression": """
                (function(){
                    const p = document.getElementById('figma-auto-panel');
                    if(p){p.remove(); delete window.FIGMA_AUTO; return 'removed';}
                    return 'clean';
                })()
            """, "returnByValue": True}
        }))
        resp = json.loads(await ws.recv())
        status = resp.get("result",{}).get("result",{}).get("value","")
        print(f"  Cleanup: {status}")

        # Inject
        await ws.send(json.dumps({
            "id": 2, "method": "Runtime.evaluate",
            "params": {"expression": script, "returnByValue": False}
        }))
        resp = json.loads(await ws.recv())
        if resp.get("result",{}).get("exceptionDetails"):
            print(f"FAILED: {resp['result']['exceptionDetails']}")
            return 1

        await asyncio.sleep(3)

        # Verify
        await ws.send(json.dumps({
            "id": 3, "method": "Runtime.evaluate",
            "params": {"expression": "!!document.getElementById('figma-auto-panel') && !!window.FIGMA_AUTO",
                        "returnByValue": True}
        }))
        resp = json.loads(await ws.recv())
        if not resp.get("result",{}).get("result",{}).get("value"):
            print("FAILED: Script did not initialize")
            return 1
        print("  Verified")
        print()

        # Step 5: Mock FS
        print("[5/7] Installing secure File System mock...")
        await ws.send(json.dumps({
            "id": 4, "method": "Runtime.evaluate",
            "params": {"expression": build_mock_js(), "returnByValue": True}
        }))
        resp = json.loads(await ws.recv())
        if resp.get("result",{}).get("exceptionDetails"):
            print(f"FAILED: {resp['result']['exceptionDetails']}")
            return 1
        print("  Mock installed (token-auth + anti-throttle)")
        print()

        # Step 6: Select folder
        print("[6/7] Selecting output folder...")
        await ws.send(json.dumps({
            "id": 5, "method": "Runtime.evaluate",
            "params": {
                "expression": "FIGMA_AUTO.selectFolder()",
                "awaitPromise": True, "returnByValue": True, "userGesture": True
            }
        }))
        await ws.recv()
        await asyncio.sleep(1)

        await ws.send(json.dumps({
            "id": 6, "method": "Runtime.evaluate",
            "params": {"expression": "JSON.parse(FIGMA_AUTO.status()).folderReady", "returnByValue": True}
        }))
        resp = json.loads(await ws.recv())
        ready = resp.get("result",{}).get("result",{}).get("value", False)
        print(f"  Folder ready: {ready}")
        print()

        # Step 7: Start
        print(f"[7/7] Starting automation from prompt {START_FROM}...")
        await ws.send(json.dumps({
            "id": 7, "method": "Runtime.evaluate",
            "params": {
                "expression": f"FIGMA_AUTO.start({START_FROM})",
                "awaitPromise": False, "returnByValue": True, "userGesture": True
            }
        }))
        await ws.recv()
        await asyncio.sleep(3)

        # Initial status
        await ws.send(json.dumps({
            "id": 8, "method": "Runtime.evaluate",
            "params": {"expression": "FIGMA_AUTO.status()", "returnByValue": True}
        }))
        resp = json.loads(await ws.recv())
        val = resp.get("result",{}).get("result",{}).get("value","")
        try:
            st = json.loads(val) if isinstance(val, str) else val
            print()
            print("=" * 60)
            print("  AUTOMATION RUNNING")
            print("=" * 60)
            print(f"  Prompt: {st.get('nextPromptId')}/{st.get('totalPrompts')}")
            print(f"  Folder: {st.get('folderName')} (ready: {st.get('folderReady')})")
            print(f"  Auto-shutdown: ON (max {AUTO_SHUTDOWN_TIMEOUT//3600}h)")
            print(f"  Monitoring every {MONITOR_INTERVAL}s...")
            print()
        except:
            print(f"  Status: {val}")

    # ─── Monitor and auto-shutdown ───
    result = await monitor_until_complete(ws_url)

    print()
    print("=" * 60)
    print("  SHUTTING DOWN")
    print("=" * 60)

    # Count output files
    file_count = 0
    total_size = 0
    for root, dirs, files in os.walk(OUTPUT_PATH):
        for f in files:
            fp = os.path.join(root, f)
            file_count += 1
            total_size += os.path.getsize(fp)
    print(f"  Output: {file_count} files ({total_size:,} bytes)")
    print(f"  Result: {result}")

    # Shutdown file server
    print("  Stopping file server...")
    server.shutdown()

    # Shutdown Chrome CDP
    shutdown_chrome()

    print("  All services stopped.")
    print("=" * 60)
    return 0


# ═══════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(run())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n  Manual interrupt - shutting down...")
        shutdown_chrome()
        sys.exit(0)
    except Exception as e:
        print(f"\n  Fatal error: {e}")
        import traceback
        traceback.print_exc()
        shutdown_chrome()
        sys.exit(1)
