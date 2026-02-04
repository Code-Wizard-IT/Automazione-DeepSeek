# DeepSeek Automation v2.1 - Secure Edition

Automated prompt execution on DeepSeek chat with CDP injection, local file saving, and security hardening.

## Features

- **12 Figma catalog prompts** executed automatically in sequence
- **CDP injection** - injects 139KB script via Chrome DevTools Protocol (no chunking)
- **Triple-Lock export** - detects response completion with 3 independent checks
- **Anti-detection** - typing jitter, random pauses, periodic breaks
- **Nav-verify** - 4-strategy navigation with verification
- **Secure file server** - token-auth, path validation, CORS restricted
- **Anti-throttle** - works with Chrome minimized (visibility mock + Chrome flags)
- **Auto-shutdown** - closes Chrome + server when automation completes
- **Resume support** - restart from any prompt number

## Quick Start

### First time setup

1. Install Python dependency: `pip install websockets`
2. Run once to create Chrome CDP profile: script will open Chrome, log into DeepSeek manually
3. Login persists in `C:\Users\cresc\ChromeCDP\`

### Run automation

```bash
# Full run (all 12 prompts)
python start_full_automation.py

# Resume from prompt N
python start_full_automation.py 5

# Check status while running
python check_status.py
```

### What happens

1. Starts secure file server on `127.0.0.1:8765` (token-auth)
2. Launches Chrome with CDP + anti-throttle flags
3. Injects automation script (139KB) via WebSocket
4. Mocks File System API to redirect file writes to local server
5. Starts automation from specified prompt
6. Monitors progress, auto-shutdowns when complete

## Files

| File | Purpose |
|------|---------|
| `start_full_automation.py` | **Main launcher** - CDP + file server + monitor + auto-shutdown |
| `build_script_v2.1.py` | Build script - assembles .user.js from template + prompts |
| `launch_automation.py` | Simple CDP injector (no file server, no monitor) |
| `launch_chrome_cdp.bat` | Manual Chrome CDP launcher |
| `check_status.py` | Check automation status via CDP |
| `preflight_check.py` | Verify all files are present |
| `prompts/` | 12 Figma prompt markdown files |

## Security

- File server: per-session random token (64-char hex)
- CORS: restricted to `https://chat.deepseek.com`
- Path traversal: blocked (`..`, absolute paths, null bytes)
- Request size: 5MB max
- CDP origins: restricted
- Auto-shutdown: 4-hour safety timeout
- Crash detection: monitors CDP, shuts down on disconnect

## Rebuilding the script

If you modify prompts or template:

```bash
python build_script_v2.1.py
python preflight_check.py
```

Output: `figma-deepseek-automation-v2.1.user.js` on Desktop

## Architecture

```
start_full_automation.py
    |
    +-- Chrome CDP (port 9222)
    |       |
    |       +-- DeepSeek tab
    |       |       |
    |       |       +-- Injected automation script
    |       |       +-- Mock File System API
    |       |       +-- Anti-throttle (visibility mock)
    |       |
    |       +-- WebSocket monitoring
    |
    +-- File Server (port 8765, localhost only)
            |
            +-- Token-authenticated writes
            +-- Path-validated output
            +-- output deepseek/new/
```
