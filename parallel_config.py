# ================================================================
# parallel_config.py - Configuration for parallel multi-worker automation
# ================================================================
# Supports 2-4 parallel Chrome instances with different profiles
# Each worker processes a subset of prompts independently
# ================================================================

import os
from config import (
    PROMPT_DIR, PROMPT_FILE_PREFIX, PROMPT_FILE_SUFFIX, PROMPT_COUNT,
    OUTPUT_DIR, DISPLAY_PREFIX, SCRIPT_NAME, SCRIPT_VERSION,
    TYPING_DELAY_MIN, TYPING_DELAY_MAX,
    INTER_PROMPT_PAUSE_MIN, INTER_PROMPT_PAUSE_MAX,
    LONG_BREAK_EVERY, LONG_BREAK_MIN, LONG_BREAK_MAX,
    MAX_REQUEST_SIZE, AUTO_SHUTDOWN_TIMEOUT, MONITOR_INTERVAL,
    CHROME_PATH, DEEPSEEK_URL
)

# ─── Parallel Configuration ──────────────────────────────────
# Number of parallel workers (2-4)
NUM_WORKERS = 2

# Base ports (each worker gets +1 offset)
CDP_PORT_BASE = 9222          # Worker 1: 9222, Worker 2: 9223, etc.
FILE_SERVER_PORT_BASE = 8765  # Worker 1: 8765, Worker 2: 8766, etc.

# Chrome profile base directory (append worker number: ChromeCDP1, ChromeCDP2...)
CHROME_PROFILE_BASE = r"C:\Users\YourName\ChromeCDP"

# Output subdirectory pattern (use {worker_id} placeholder)
OUTPUT_SUBDIR_PATTERN = "worker_{worker_id}"

# Merge outputs after completion?
MERGE_OUTPUTS = True
MERGED_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "merged")

# ─── Worker Configuration Generator ──────────────────────────
def get_worker_config(worker_id: int, prompt_range: tuple) -> dict:
    """
    Generate configuration for a specific worker.
    
    Args:
        worker_id: Worker number (1-based)
        prompt_range: Tuple of (start_prompt, end_prompt) inclusive
    
    Returns:
        Dictionary with all worker-specific settings
    """
    return {
        'worker_id': worker_id,
        'cdp_port': CDP_PORT_BASE + (worker_id - 1),
        'file_server_port': FILE_SERVER_PORT_BASE + (worker_id - 1),
        'chrome_profile': f"{CHROME_PROFILE_BASE}{worker_id}",
        'output_dir': os.path.join(OUTPUT_DIR, OUTPUT_SUBDIR_PATTERN.format(worker_id=worker_id)),
        'prompt_start': prompt_range[0],
        'prompt_end': prompt_range[1],
        'prompt_count': prompt_range[1] - prompt_range[0] + 1,
    }


def distribute_prompts(total_prompts: int, num_workers: int) -> list:
    """
    Distribute prompts evenly across workers.
    
    Returns:
        List of (start, end) tuples for each worker
    """
    if num_workers < 1 or num_workers > 4:
        raise ValueError("num_workers must be between 1 and 4")
    
    if total_prompts < num_workers:
        return [(i, i) for i in range(1, total_prompts + 1)]
    
    base_count = total_prompts // num_workers
    remainder = total_prompts % num_workers
    
    ranges = []
    current = 1
    
    for i in range(num_workers):
        count = base_count + (1 if i < remainder else 0)
        end = current + count - 1
        ranges.append((current, end))
        current = end + 1
    
    return ranges


def get_all_worker_configs(num_workers: int = NUM_WORKERS) -> list:
    """
    Generate configurations for all workers.
    
    Returns:
        List of worker configuration dictionaries
    """
    prompt_ranges = distribute_prompts(PROMPT_COUNT, num_workers)
    return [
        get_worker_config(i + 1, prompt_ranges[i])
        for i in range(len(prompt_ranges))
    ]


# ─── Validation ──────────────────────────────────────────────
def validate_config():
    """Validate parallel configuration"""
    errors = []
    
    if NUM_WORKERS < 1 or NUM_WORKERS > 4:
        errors.append(f"NUM_WORKERS must be 1-4, got {NUM_WORKERS}")
    
    if PROMPT_COUNT < 1:
        errors.append(f"PROMPT_COUNT must be >= 1, got {PROMPT_COUNT}")
    
    used_ports = set()
    for i in range(NUM_WORKERS):
        cdp = CDP_PORT_BASE + i
        fs = FILE_SERVER_PORT_BASE + i
        if cdp in used_ports:
            errors.append(f"CDP port conflict: {cdp}")
        if fs in used_ports:
            errors.append(f"File server port conflict: {fs}")
        used_ports.add(cdp)
        used_ports.add(fs)
    
    return errors


# ─── Display Info ────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  Parallel Configuration Preview")
    print("=" * 60)
    
    errors = validate_config()
    if errors:
        print("\n⚠️  Configuration Errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print(f"\n  Workers: {NUM_WORKERS}")
        print(f"  Total prompts: {PROMPT_COUNT}")
        print()
        
        for cfg in get_all_worker_configs():
            print(f"  Worker {cfg['worker_id']}:")
            print(f"    CDP Port: {cfg['cdp_port']}")
            print(f"    File Server: {cfg['file_server_port']}")
            print(f"    Chrome Profile: {cfg['chrome_profile']}")
            print(f"    Prompts: {cfg['prompt_start']}-{cfg['prompt_end']} ({cfg['prompt_count']} total)")
            print(f"    Output: {cfg['output_dir']}")
            print()
