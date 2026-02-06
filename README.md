# DeepSeek Automation - Parallel Template

Automated prompt execution on DeepSeek chat via Chrome DevTools Protocol.  
Supports **parallel execution** with 2-4 Chrome instances for faster processing.

## Features

- **Parallel execution** - Run 2-4 workers simultaneously
- **CDP injection** - Injects script via Chrome DevTools Protocol
- **Triple-Lock export** - 3 independent completion checks before saving
- **Anti-detection** - Typing jitter, random pauses, periodic breaks
- **Nav-verify** - 4-strategy navigation with verification cascade
- **Secure file server** - Per-session token auth, path validation, CORS restricted
- **Auto-shutdown** - Closes Chrome + server when automation completes
- **Resume support** - Restart from any prompt number

## Quick Start

### 1. Configure

Edit `config.py` with your paths:

```python
PROMPT_DIR = r"C:\path\to\your\prompts"
OUTPUT_SCRIPT = r"C:\path\to\output\deepseek-automation.user.js"
OUTPUT_DIR = r"C:\path\to\output\responses"
PROMPT_FILE_PREFIX = "PROMPT-PROJECT-"
PROMPT_COUNT = 10
```

Edit `parallel_config.py` for parallel settings:

```python
NUM_WORKERS = 2  # 2-4 workers
CHROME_PROFILE_BASE = r"C:\Users\YourName\ChromeCDP"
```

### 2. Add Prompts

Place `.md` files in your `PROMPT_DIR` folder:

```
PROMPT-PROJECT-01-INTRO.md
PROMPT-PROJECT-02-CONTENT.md
PROMPT-PROJECT-03-CONCLUSION.md
```

### 3. Build Script

```bash
python build_template.py
```

### 4. Setup Chrome Profiles (First Time)

```bash
# Preview what's needed
python parallel_automation.py --dry-run
```

For each worker, open Chrome with a dedicated profile and log into DeepSeek:

```powershell
# PowerShell
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "--user-data-dir=C:\Users\YourName\ChromeCDP1","--remote-debugging-port=9222","https://chat.deepseek.com"
```

### 5. Run Parallel Automation

```bash
# Default (2 workers)
python parallel_automation.py

# Use 3 workers
python parallel_automation.py --workers 3

# Preview configuration
python parallel_automation.py --dry-run
```

## Files

| File | Purpose |
|------|---------|
| `config.py` | Main configuration - paths, naming, timing |
| `parallel_config.py` | Parallel worker settings |
| `build_template.py` | Builds .user.js from config + prompts |
| `parallel_automation.py` | **Main launcher** - orchestrates parallel workers |
| `worker_automation.py` | Single worker instance |
| `check_status.py` | Real-time status checker |
| `preflight_check.py` | Verify all files before launch |
| `prompts/` | Example prompt files |
| `old/` | Previous versions |

## Parallel Architecture

```
parallel_automation.py (orchestrator)
    |
    +-- Worker 1
    |   +-- Chrome (CDP port 9222)
    |   +-- File Server (port 8765)
    |   +-- Prompts 1-5
    |
    +-- Worker 2
    |   +-- Chrome (CDP port 9223)
    |   +-- File Server (port 8766)
    |   +-- Prompts 6-10
    |
    +-- Merge outputs -> merged/
```

## Security

| Layer | Protection |
|-------|------------|
| File server | Per-session random token (64-char hex) |
| CORS | Restricted to DeepSeek origin only |
| Path validation | Blocks traversal attacks |
| Request size | 5MB max per write |
| CDP | Dedicated Chrome profile (isolated) |
| Runtime | 4-hour safety timeout |

## Requirements

- Python 3.8+
- `pip install websockets`
- Google Chrome
- DeepSeek account

## Documentation

- [PARALLEL-README.md](PARALLEL-README.md) - Detailed parallel setup guide
- [PROMPT-QUICK-START.md](PROMPT-QUICK-START.md) - Quick prompt creation guide
- [prompts/README.md](prompts/README.md) - Prompt naming conventions
