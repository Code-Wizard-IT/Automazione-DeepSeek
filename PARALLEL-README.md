# Parallel Automation Guide

Execute multiple DeepSeek automation instances simultaneously using different Chrome profiles.

## Quick Start

### 1. First-Time Profile Setup

Before running parallel automation, you need to set up Chrome profiles for each worker.
The script will detect missing profiles and show you the commands to run.

```powershell
# Run this to see which profiles are needed:
python parallel_automation.py --dry-run
```

For each missing profile, open a terminal and run:
```powershell
# Worker 1 (example)
"C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --user-data-dir="C:\Users\cresc\ChromeCDP1" ^
  --remote-debugging-port=9222 ^
  https://chat.deepseek.com

# Worker 2 (example)
"C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --user-data-dir="C:\Users\cresc\ChromeCDP2" ^
  --remote-debugging-port=9223 ^
  https://chat.deepseek.com
```

Log into DeepSeek in each Chrome window, then close them.

### 2. Build the Script

```powershell
python build_template.py
```

### 3. Run Parallel Automation

```powershell
# Default (2 workers)
python parallel_automation.py

# Use 3 workers
python parallel_automation.py --workers 3

# Preview configuration without running
python parallel_automation.py --dry-run

# Run sequentially for debugging
python parallel_automation.py --sequential

# Skip merging outputs
python parallel_automation.py --no-merge
```

## How It Works

### Prompt Distribution

Prompts are distributed evenly across workers:

| Workers | Prompts | Worker 1 | Worker 2 | Worker 3 | Worker 4 |
|---------|---------|----------|----------|----------|----------|
| 2       | 12      | 1-6      | 7-12     | -        | -        |
| 3       | 12      | 1-4      | 5-8      | 9-12     | -        |
| 4       | 12      | 1-3      | 4-6      | 7-9      | 10-12    |

### Architecture

```
parallel_automation.py (orchestrator)
    |
    +-- Worker 1
    |   +-- Chrome (CDP port 9222)
    |   +-- File Server (port 8765)
    |   +-- Profile: ChromeCDP1
    |   +-- Output: output/worker_1/
    |
    +-- Worker 2
    |   +-- Chrome (CDP port 9223)
    |   +-- File Server (port 8766)
    |   +-- Profile: ChromeCDP2
    |   +-- Output: output/worker_2/
    |
    +-- (Worker 3, 4 if configured)
    |
    +-- Merge outputs -> output/merged/
```

## Configuration

Edit `parallel_config.py` to customize:

```python
# Number of parallel workers (2-4)
NUM_WORKERS = 2

# Base ports (each worker gets +1 offset)
CDP_PORT_BASE = 9222          # Worker 1: 9222, Worker 2: 9223
FILE_SERVER_PORT_BASE = 8765  # Worker 1: 8765, Worker 2: 8766

# Chrome profile directory pattern
CHROME_PROFILE_BASE = r"C:\Users\cresc\ChromeCDP"

# Merge outputs after completion
MERGE_OUTPUTS = True
```

## Files

| File | Purpose |
|------|---------|
| `parallel_config.py` | Parallel worker configuration |
| `parallel_automation.py` | Main orchestrator script |
| `worker_automation.py` | Single worker instance |
| `build_template.py` | Build the automation script |

## Output Structure

During execution:
```
output/
├── worker_1/
│   ├── 01-FUNDAMENTALS/
│   │   ├── FUNDAMENTALS-parte-1.txt
│   │   └── FUNDAMENTALS-parte-2.txt
│   └── 02-TYPOGRAPHY/
│       └── ...
├── worker_2/
│   ├── 07-BRAND-IDENTITY/
│   └── ...
└── merged/    (created after completion)
    ├── 01-FUNDAMENTALS/
    ├── 02-TYPOGRAPHY/
    └── ...
```

## Troubleshooting

### "Profile not found" errors
Run the profile setup commands shown by `--dry-run`.

### Port conflicts
Ensure no other Chrome instances are using ports 9222-9225.

### Worker crashes
Check individual worker logs. Each worker prefixes output with `[W1]`, `[W2]`, etc.

### Merge fails
Outputs remain in individual `worker_N/` folders if merge fails.

## Tips

1. **Start with 2 workers** - Test with 2 before scaling to 3-4
2. **Monitor progress** - Watch console for `[W1]`, `[W2]` prefixed logs
3. **Kill stuck workers** - Use Task Manager to close Chrome if needed
4. **Resume support** - Each worker can resume from where it left off

## Speed Comparison

| Configuration | 12 Prompts | Effective Speedup |
|--------------|------------|-------------------|
| Single       | ~2 hours   | 1x                |
| 2 Workers    | ~1 hour    | ~1.8x             |
| 3 Workers    | ~45 min    | ~2.5x             |
| 4 Workers    | ~35 min    | ~3x               |

*Note: Actual speedup depends on prompt complexity and rate limits.*
