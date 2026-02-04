# ================================================================
# config.py - Centralized configuration for DeepSeek Automation
# ================================================================
# Edit this file to customize paths, naming, and behavior.
# All other scripts read from here.
# ================================================================

import os

# ─── Paths ────────────────────────────────────────────────
# Where your prompt .md files are stored
PROMPT_DIR = r"C:\Users\cresc\Desktop\Prompt"

# Output .user.js script path
OUTPUT_SCRIPT = r"C:\Users\cresc\Desktop\deepseek-automation.user.js"

# Where DeepSeek responses are saved
OUTPUT_DIR = r"C:\Users\cresc\Desktop\output deepseek\new"

# Chrome CDP dedicated profile (login to DeepSeek once, persists)
CHROME_USER_DATA = r"C:\Users\cresc\ChromeCDP"

# ─── Prompt naming ────────────────────────────────────────
# Files must match: {PREFIX}{NN}-{TOPIC}.md
# Example: PROMPT-FIGMA-01-FUNDAMENTALS.md
PROMPT_FILE_PREFIX = "PROMPT-FIGMA-"
PROMPT_FILE_SUFFIX = ".md"

# Display name prefix in generated script (e.g. "FIGMA-01-FUNDAMENTALS")
DISPLAY_PREFIX = "FIGMA-"

# How many prompts (1 to N)
PROMPT_COUNT = 12

# ─── Script metadata ─────────────────────────────────────
SCRIPT_NAME = "DeepSeek Automation"
SCRIPT_VERSION = "2.1"
SCRIPT_DESCRIPTION = "Automated prompt execution on DeepSeek"

# ─── CDP & Server ────────────────────────────────────────
CDP_PORT = 9222
FILE_SERVER_PORT = 8765
DEEPSEEK_URL = "chat.deepseek.com"

# ─── Anti-detection ──────────────────────────────────────
TYPING_DELAY_MIN = 30       # ms
TYPING_DELAY_MAX = 90       # ms
INTER_PROMPT_PAUSE_MIN = 10  # seconds
INTER_PROMPT_PAUSE_MAX = 30  # seconds
LONG_BREAK_EVERY = 8        # prompts
LONG_BREAK_MIN = 180         # seconds
LONG_BREAK_MAX = 300         # seconds

# ─── Security ────────────────────────────────────────────
MAX_REQUEST_SIZE = 5 * 1024 * 1024   # 5MB per file write
AUTO_SHUTDOWN_TIMEOUT = 4 * 3600      # 4 hours max runtime
MONITOR_INTERVAL = 30                 # seconds between status checks

# ─── Derived (don't edit) ────────────────────────────────
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CDP_URL = f"http://localhost:{CDP_PORT}/json"
ALLOWED_ORIGIN = f"https://{DEEPSEEK_URL}"
