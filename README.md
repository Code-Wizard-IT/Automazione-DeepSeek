# DeepSeek Automation - Reusable Template

Automated prompt execution on DeepSeek chat via Chrome DevTools Protocol.  
Inject any set of prompts, get structured text responses saved locally.

## Quick Start

### 1. Configure
Edit `config.py` with your paths:
```python
PROMPT_DIR = r"C:\path\to\your\prompts"
OUTPUT_SCRIPT = r"C:\path\to\output.user.js"
OUTPUT_DIR = r"C:\path\to\saved\responses"
PROMPT_FILE_PREFIX = "PROMPT-FIGMA-"  # your naming pattern
PROMPT_COUNT = 12                      # how many prompts
```

### 2. Add prompts
Place `.md` files in your `PROMPT_DIR` folder:
```
PROMPT-FIGMA-01-FUNDAMENTALS.md
PROMPT-FIGMA-02-TYPOGRAPHY.md
...
```
See `prompts/README.md` for naming details.

### 3. Build
```bash
python build_template.py
```
Generates the `.user.js` automation script.

### 4. Run
```bash
# First time: creates Chrome CDP profile, log into DeepSeek manually
python start_full_automation.py

# Resume from prompt N
python start_full_automation.py 5

# Check status while running
python check_status.py
```

## Features

- **CDP injection** - injects script via Chrome DevTools Protocol (no Tampermonkey needed)
- **Triple-Lock export** - 3 independent completion checks before saving
- **Anti-detection** - typing jitter, random pauses, periodic breaks
- **Nav-verify** - 4-strategy navigation with verification cascade
- **Secure file server** - per-session token auth, path validation, CORS restricted
- **Anti-throttle** - works with Chrome minimized
- **Auto-shutdown** - closes Chrome + server when automation completes
- **Resume support** - restart from any prompt number

## Files

| File | Purpose |
|------|---------|
| `config.py` | **All settings** - paths, naming, timing, security |
| `build_template.py` | Build script - assembles .user.js from config + prompts |
| `start_full_automation.py` | Main launcher - CDP + file server + monitor + auto-shutdown |
| `launch_automation.py` | Simple CDP injector (no file server) |
| `launch_chrome_cdp.bat` | Manual Chrome CDP launcher |
| `check_status.py` | Real-time status checker via CDP |
| `preflight_check.py` | Verify all files present before launch |
| `prompts/` | Example prompt files |

## Security

| Layer | Protection |
|-------|-----------|
| File server | Per-session random token (64-char hex) |
| CORS | Restricted to DeepSeek origin only |
| Path validation | Blocks traversal (`..`, abs paths, null bytes) |
| Request size | 5MB max per write |
| CDP | Dedicated Chrome profile (isolated from main browser) |
| Runtime | 4-hour safety timeout, crash detection |

## Architecture

```
start_full_automation.py
    |
    +-- Chrome CDP (port 9222)
    |       |-- DeepSeek tab
    |       |-- Injected automation script (.user.js)
    |       |-- Mock File System API
    |       +-- Anti-throttle (visibility mock)
    |
    +-- File Server (port 8765, localhost only)
            +-- Token-authenticated writes -> OUTPUT_DIR
```

## Requirements

- Python 3.8+
- `pip install websockets`
- Google Chrome
- DeepSeek account (free tier works)
