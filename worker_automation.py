#!/usr/bin/env python3
"""
Worker Automation - Single worker instance for parallel execution
Receives configuration via command line args or environment variables

Usage:
    python worker_automation.py --worker-id 1 --cdp-port 9222 --fs-port 8765 \
        --profile C:\ChromeCDP1 --output C:\output\worker_1 \
        --start 1 --end 6 --script C:\path\to\script.user.js
"""

import argparse
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
# PARSE ARGUMENTS
# ═══════════════════════════════════════════════════════════

def parse_args():
    parser = argparse.ArgumentParser(description='DeepSeek Worker Automation')
    parser.add_argument('--worker-id', type=int, required=True, help='Worker ID (1-4)')
    parser.add_argument('--cdp-port', type=int, required=True, help='Chrome CDP port')
    parser.add_argument('--fs-port', type=int, required=True, help='File server port')
    parser.add_argument('--profile', type=str, required=True, help='Chrome profile directory')
    parser.add_argument('--output', type=str, required=True, help='Output directory')
    parser.add_argument('--start', type=int, required=True, help='Start prompt number')
    parser.add_argument('--end', type=int, required=True, help='End prompt number')
    parser.add_argument('--script', type=str, required=True, help='Path to .user.js script')
    parser.add_argument('--quiet', action='store_true', help='Reduce output verbosity')
    return parser.parse_args()

ARGS = parse_args()

# ═══════════════════════════════════════════════════════════
# CONFIGURATION FROM ARGS
# ═══════════════════════════════════════════════════════════

WORKER_ID = ARGS.worker_id
CDP_PORT = ARGS.cdp_port
CDP_URL = f"http://localhost:{CDP_PORT}/json"
FILE_SERVER_PORT = ARGS.fs_port
CHROME_USER_DATA = ARGS.profile
OUTPUT_PATH = ARGS.output
SCRIPT_PATH = ARGS.script
START_PROMPT = ARGS.start
END_PROMPT = ARGS.end
QUIET = ARGS.quiet

DEEPSEEK_URL = "chat.deepseek.com"
CDP_TIMEOUT = 30
MAX_REQUEST_SIZE = 5 * 1024 * 1024
AUTO_SHUTDOWN_TIMEOUT = 4 * 3600
MONITOR_INTERVAL = 30
ALLOWED_ORIGIN = f"https://{DEEPSEEK_URL}"

AUTH_TOKEN = secrets.token_hex(32)

def log(msg):
    if not QUIET:
        print(f"[W{WORKER_ID}] {msg}")

def log_always(msg):
    print(f"[W{WORKER_ID}] {msg}")


# ═══════════════════════════════════════════════════════════
# SECURE FILE SERVER
# ═══════════════════════════════════════════════════════════

def is_safe_path(component):
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
        self.send_response(405)
        self.end_headers()

    def do_POST(self):
        token = self.headers.get('X-Auth-Token', '')
        if token != AUTH_TOKEN:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'{"error":"unauthorized"}')
            return

        length = int(self.headers.get('Content-Length', 0))
        if length > MAX_REQUEST_SIZE:
            self.send_response(413)
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error":"too large"}')
            return

        try:
            data = json.loads(self.rfile.read(length))
            folder = data.get('folder', '')
            filename = data.get('filename', '')
            content = data.get('content', '')

            if not is_safe_path(folder) or not is_safe_path(filename):
                self.send_response(400)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"error":"invalid path"}')
                return

            if not filename:
                self.send_response(400)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"error":"no filename"}')
                return

            target_dir = os.path.join(OUTPUT_PATH, folder) if folder else OUTPUT_PATH
            resolved = os.path.realpath(target_dir)
            if not resolved.startswith(os.path.realpath(OUTPUT_PATH)):
                self.send_response(403)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"error":"path escape"}')
                return

            os.makedirs(target_dir, exist_ok=True)
            filepath = os.path.join(target_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            size = len(content.encode('utf-8'))
            log(f"[FILE] {filename} ({size:,} bytes)")

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True}).encode())

        except Exception as e:
            log(f"[ERROR] {e}")
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
    log("Launching Chrome with CDP...")
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
    log("Shutting down Chrome...")
    try:
        # Find and kill only our Chrome instance by profile
        result = subprocess.run(
            ['wmic', 'process', 'where', 
             f"commandline like '%--user-data-dir={CHROME_USER_DATA.replace(chr(92), chr(92)+chr(92))}%'",
             'get', 'processid'],
            capture_output=True, text=True, timeout=10
        )
        for line in result.stdout.strip().split('\n')[1:]:
            pid = line.strip()
            if pid.isdigit():
                subprocess.run(['taskkill', '/F', '/PID', pid], capture_output=True, timeout=5)
    except Exception as e:
        log(f"Chrome shutdown error: {e}")


def wait_for_cdp(timeout=CDP_TIMEOUT):
    log(f"Waiting for CDP (timeout: {timeout}s)...")
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
        log(f"Error reading script: {e}")
        return None


# ═══════════════════════════════════════════════════════════
# MOCK JS (with auth token + anti-throttle)
# ═══════════════════════════════════════════════════════════

def build_mock_js():
    return """
(function() {
    Object.defineProperty(document, 'hidden', { get: () => false, configurable: true });
    Object.defineProperty(document, 'visibilityState', { get: () => 'visible', configurable: true });
    document.addEventListener('visibilitychange', function(e) { e.stopImmediatePropagation(); }, true);
    const origRAF = window.requestAnimationFrame;
    window.requestAnimationFrame = function(cb) {
        return origRAF ? origRAF.call(window, cb) : setTimeout(cb, 16);
    };

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
        return new MockDirectoryHandle('', '');
    };

    console.log('[MockFS] Worker __WORKER_ID__ ready');
    return true;
})();
""".replace('__PORT__', str(FILE_SERVER_PORT)).replace('__TOKEN__', AUTH_TOKEN).replace('__WORKER_ID__', str(WORKER_ID))


# ═══════════════════════════════════════════════════════════
# STATUS MONITOR
# ═══════════════════════════════════════════════════════════

async def monitor_until_complete(ws_url):
    import websockets

    start_time = time.time()
    last_prompt = 0

    while True:
        elapsed = time.time() - start_time

        if elapsed > AUTO_SHUTDOWN_TIMEOUT:
            log_always(f"[TIMEOUT] Max runtime reached")
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

                if current != last_prompt:
                    mins = int(elapsed // 60)
                    log(f"[{mins}m] Prompt {current}/{total} | Exported: {exported}")
                    last_prompt = current

                if not running and exported > 0:
                    log_always(f"✅ Finished! {exported} files in {int(elapsed//60)}m")
                    return 'complete'

        except Exception as e:
            log(f"[WARNING] CDP connection lost: {e}")
            return 'disconnected'

        await asyncio.sleep(MONITOR_INTERVAL)


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

async def run():
    import websockets

    log_always("=" * 50)
    log_always(f"Worker {WORKER_ID} Starting")
    log_always(f"  Prompts: {START_PROMPT}-{END_PROMPT}")
    log_always(f"  CDP Port: {CDP_PORT} | FS Port: {FILE_SERVER_PORT}")
    log_always(f"  Output: {OUTPUT_PATH}")
    log_always("=" * 50)

    # Step 1: File server
    log("Starting file server...")
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    server = start_file_server()
    log(f"File server on port {FILE_SERVER_PORT}")

    # Step 2: CDP
    log("Connecting to Chrome CDP...")
    if not check_cdp():
        launch_chrome()
        if not wait_for_cdp():
            log_always("FAILED: Chrome CDP did not start")
            return 1
    else:
        log("CDP already running")

    await asyncio.sleep(2)

    # Step 3: Find tab
    log("Finding DeepSeek tab...")
    tabs = get_tabs()
    tab = find_deepseek_tab(tabs)
    if not tab:
        log("Opening DeepSeek tab...")
        url = f"http://localhost:{CDP_PORT}/json/new?https://{DEEPSEEK_URL}"
        with urllib.request.urlopen(url, timeout=10) as r:
            json.loads(r.read().decode())
        await asyncio.sleep(5)
        tabs = get_tabs()
        tab = find_deepseek_tab(tabs)
        if not tab:
            log_always("FAILED: Cannot find DeepSeek tab")
            return 1
    
    ws_url = tab["webSocketDebuggerUrl"]
    log(f"Connected to: {tab.get('title', 'Unknown')}")

    # Step 4: Inject script
    log("Injecting automation script...")
    script = read_script()
    if not script:
        return 1

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
        await ws.recv()

        # Inject
        await ws.send(json.dumps({
            "id": 2, "method": "Runtime.evaluate",
            "params": {"expression": script, "returnByValue": False}
        }))
        resp = json.loads(await ws.recv())
        if resp.get("result",{}).get("exceptionDetails"):
            log_always(f"FAILED: Script error")
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
            log_always("FAILED: Script did not initialize")
            return 1
        log("Script verified")

        # Step 5: Mock FS
        log("Installing mock filesystem...")
        await ws.send(json.dumps({
            "id": 4, "method": "Runtime.evaluate",
            "params": {"expression": build_mock_js(), "returnByValue": True}
        }))
        await ws.recv()

        # Step 6: Select folder
        await ws.send(json.dumps({
            "id": 5, "method": "Runtime.evaluate",
            "params": {
                "expression": "FIGMA_AUTO.selectFolder()",
                "awaitPromise": True, "returnByValue": True, "userGesture": True
            }
        }))
        await ws.recv()
        await asyncio.sleep(1)

        # Step 7: Start automation
        log_always(f"Starting automation: prompts {START_PROMPT}-{END_PROMPT}")
        await ws.send(json.dumps({
            "id": 7, "method": "Runtime.evaluate",
            "params": {
                "expression": f"FIGMA_AUTO.startRange({START_PROMPT}, {END_PROMPT})",
                "awaitPromise": False, "returnByValue": True, "userGesture": True
            }
        }))
        await ws.recv()
        await asyncio.sleep(3)

    # Monitor
    result = await monitor_until_complete(ws_url)

    # Cleanup
    log("Shutting down...")
    server.shutdown()
    shutdown_chrome()

    # Stats
    file_count = 0
    total_size = 0
    for root, dirs, files in os.walk(OUTPUT_PATH):
        for f in files:
            fp = os.path.join(root, f)
            file_count += 1
            total_size += os.path.getsize(fp)
    
    log_always(f"Output: {file_count} files ({total_size:,} bytes)")
    log_always(f"Result: {result}")
    
    return 0 if result == 'complete' else 1


# ═══════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(run())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        log_always("Interrupted")
        shutdown_chrome()
        sys.exit(0)
    except Exception as e:
        log_always(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        shutdown_chrome()
        sys.exit(1)
