#!/usr/bin/env python3
"""
CDP Injector for DeepSeek Automation
Injects the Figma automation script into chat.deepseek.com via Chrome DevTools Protocol
"""

import asyncio
import json
import subprocess
import sys
import time
import urllib.request
import urllib.error

# Fix Windows encoding for emoji support
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Configuration
CDP_PORT = 9222
CDP_URL = f"http://localhost:{CDP_PORT}/json"
CHROME_LAUNCHER = r"C:\Users\cresc\Desktop\launch_chrome_cdp.bat"
SCRIPT_PATH = r"C:\Users\cresc\Desktop\figma-deepseek-automation-v2.1.user.js"
DEEPSEEK_URL = "chat.deepseek.com"
CDP_TIMEOUT = 30  # seconds to wait for CDP to be ready
CHROME_USER_DATA = r"C:\Users\cresc\ChromeCDP"


def check_cdp_available():
    """Check if Chrome CDP is responding on port 9222"""
    try:
        with urllib.request.urlopen(CDP_URL, timeout=2) as response:
            return response.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        return False


def launch_chrome():
    """Launch Chrome via the batch file, handling existing Chrome instances"""
    # Check if Chrome is running without CDP
    try:
        result = subprocess.run(
            ['tasklist', '/FI', 'IMAGENAME eq chrome.exe'],
            capture_output=True, text=True, timeout=5
        )
        chrome_running = 'chrome.exe' in result.stdout
    except Exception:
        chrome_running = False

    if chrome_running:
        print("Chrome is running without CDP. Closing Chrome...")
        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'],
                      capture_output=True, timeout=10)
        time.sleep(3)

    print("Launching Chrome with CDP enabled...")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([
        chrome_path,
        f'--remote-debugging-port={CDP_PORT}',
        '--remote-allow-origins=*',
        f'--user-data-dir={CHROME_USER_DATA}',
        '--no-first-run',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-renderer-backgrounding',
        f'https://{DEEPSEEK_URL}'
    ])


def wait_for_cdp(timeout=CDP_TIMEOUT):
    """Wait until CDP is responding"""
    print(f"Waiting for Chrome CDP to be ready (timeout: {timeout}s)...")
    start = time.time()
    while time.time() - start < timeout:
        if check_cdp_available():
            print("Chrome CDP is ready!")
            return True
        time.sleep(0.5)
    return False


def get_tabs():
    """Get list of open tabs from CDP"""
    try:
        with urllib.request.urlopen(CDP_URL, timeout=5) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error getting tabs: {e}")
        return []


def find_deepseek_tab(tabs):
    """Find a tab with DeepSeek URL"""
    for tab in tabs:
        if tab.get("type") == "page" and DEEPSEEK_URL in tab.get("url", ""):
            return tab
    return None


def open_new_tab(url):
    """Open a new tab with the given URL"""
    try:
        new_tab_url = f"http://localhost:{CDP_PORT}/json/new?{url}"
        with urllib.request.urlopen(new_tab_url, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error opening new tab: {e}")
        return None


def read_script():
    """Read the automation script file"""
    try:
        with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Script file not found: {SCRIPT_PATH}")
        return None
    except Exception as e:
        print(f"Error reading script: {e}")
        return None


async def inject_script(websocket_url, script_content):
    """Inject the script via CDP WebSocket"""
    import websockets

    print("Connecting to tab via WebSocket...")

    async with websockets.connect(websocket_url, max_size=None) as ws:
        # First, check if script is already injected and remove it
        print("Checking for existing injection...")
        check_existing = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": """
                    (function() {
                        const panel = document.getElementById('figma-auto-panel');
                        if (panel) {
                            panel.remove();
                            delete window.FIGMA_AUTO;
                            return true;
                        }
                        return false;
                    })()
                """,
                "awaitPromise": False,
                "returnByValue": True
            }
        }

        await ws.send(json.dumps(check_existing))
        response = await ws.recv()
        result = json.loads(response)

        if result.get("result", {}).get("result", {}).get("value"):
            print("Removed existing injection")

        # Now inject the new script
        print("Injecting automation script...")
        inject_msg = {
            "id": 2,
            "method": "Runtime.evaluate",
            "params": {
                "expression": script_content,
                "awaitPromise": False,
                "returnByValue": False
            }
        }

        await ws.send(json.dumps(inject_msg))
        response = await ws.recv()
        result = json.loads(response)

        if "error" in result:
            print(f"Injection error: {result['error']}")
            return False

        # Check for exceptions in the result
        if result.get("result", {}).get("exceptionDetails"):
            exception = result["result"]["exceptionDetails"]
            print(f"Script exception: {exception.get('text', 'Unknown error')}")
            return False

        print("Script injected, waiting for initialization...")
        await asyncio.sleep(5)

        # Verify injection
        print("Verifying injection...")
        verify_msg = {
            "id": 3,
            "method": "Runtime.evaluate",
            "params": {
                "expression": "!!document.getElementById('figma-auto-panel') && !!window.FIGMA_AUTO",
                "awaitPromise": False,
                "returnByValue": True
            }
        }

        await ws.send(json.dumps(verify_msg))
        response = await ws.recv()
        result = json.loads(response)

        verified = result.get("result", {}).get("result", {}).get("value", False)
        return verified


def print_success():
    """Print success message with instructions"""
    print()
    print("=" * 50)
    print("✅ Script injected successfully!")
    print("=" * 50)
    print()
    print("Now in the browser:")
    print("1. Click 📁 on the panel (bottom-left) to select output folder")
    print("2. Click ▶ Start All to begin automation")
    print()
    print("Or use console: FIGMA_AUTO.start(1)")
    print()


def print_failure(error=None):
    """Print failure message with troubleshooting"""
    print()
    print("=" * 50)
    print("❌ Script injection failed!")
    print("=" * 50)
    if error:
        print(f"Error: {error}")
    print()
    print("Troubleshooting:")
    print("1. Make sure you're logged into chat.deepseek.com")
    print("2. Try refreshing the page and running this script again")
    print("3. Check if Chrome DevTools is already open (close it)")
    print("4. Restart Chrome and try again")
    print()


async def main():
    """Main entry point"""
    print("=" * 50)
    print("CDP Injector for DeepSeek Automation")
    print("=" * 50)
    print()

    # Step 1: Check/Launch Chrome CDP
    if not check_cdp_available():
        launch_chrome()
        if not wait_for_cdp():
            print_failure("Chrome CDP did not start within timeout")
            return 1
    else:
        print("Chrome CDP already running")

    # Small delay to let Chrome stabilize
    await asyncio.sleep(1)

    # Step 2: Find or open DeepSeek tab
    tabs = get_tabs()
    if not tabs:
        print_failure("Could not get tabs from Chrome")
        return 1

    tab = find_deepseek_tab(tabs)

    if tab:
        print(f"Found existing DeepSeek tab: {tab.get('title', 'Unknown')}")
    else:
        print("No DeepSeek tab found, opening new tab...")
        tab = open_new_tab(f"https://{DEEPSEEK_URL}")
        if not tab:
            print_failure("Could not open new tab")
            return 1

        # Wait for page to load
        print("Waiting for page to load...")
        await asyncio.sleep(5)

        # Re-fetch tabs to get updated WebSocket URL
        tabs = get_tabs()
        tab = find_deepseek_tab(tabs)
        if not tab:
            print_failure("Tab opened but could not find it in tab list")
            return 1

    websocket_url = tab.get("webSocketDebuggerUrl")
    if not websocket_url:
        print_failure("Tab does not have a WebSocket debugger URL")
        return 1

    print(f"WebSocket URL: {websocket_url}")

    # Step 3: Read the script
    script_content = read_script()
    if not script_content:
        print_failure("Could not read automation script")
        return 1

    print(f"Script loaded: {len(script_content):,} bytes")

    # Step 4: Inject the script
    try:
        success = await inject_script(websocket_url, script_content)
    except Exception as e:
        print_failure(str(e))
        return 1

    # Step 5: Print status
    if success:
        print_success()
        return 0
    else:
        print_failure("Verification check returned false - panel may not have initialized")
        return 1


if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print_failure(str(e))
        sys.exit(1)
