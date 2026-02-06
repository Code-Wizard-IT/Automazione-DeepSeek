#!/usr/bin/env python3
"""
Parallel Automation - Multi-worker orchestrator for DeepSeek
Launches 2-4 parallel Chrome instances with different profiles

Usage:
    python parallel_automation.py                  # Use config defaults
    python parallel_automation.py --workers 3     # Override worker count
    python parallel_automation.py --workers 2 --dry-run  # Preview only
"""

import argparse
import asyncio
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from parallel_config import (
    NUM_WORKERS, PROMPT_COUNT, OUTPUT_DIR, MERGED_OUTPUT_DIR, MERGE_OUTPUTS,
    get_all_worker_configs, validate_config
)
from config import OUTPUT_SCRIPT

# ═══════════════════════════════════════════════════════════
# ARGUMENT PARSING
# ═══════════════════════════════════════════════════════════

def parse_args():
    parser = argparse.ArgumentParser(
        description='Parallel DeepSeek Automation - Multi-worker orchestrator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python parallel_automation.py                    # Run with defaults
    python parallel_automation.py --workers 3       # Use 3 workers
    python parallel_automation.py --dry-run         # Preview configuration
    python parallel_automation.py --no-merge        # Skip output merging
        """
    )
    parser.add_argument('--workers', '-w', type=int, default=NUM_WORKERS,
                        choices=[1, 2, 3, 4], help='Number of parallel workers (1-4)')
    parser.add_argument('--dry-run', '-d', action='store_true',
                        help='Show configuration without running')
    parser.add_argument('--no-merge', action='store_true',
                        help='Skip merging outputs after completion')
    parser.add_argument('--sequential', '-s', action='store_true',
                        help='Run workers sequentially (for debugging)')
    parser.add_argument('--script', type=str, default=OUTPUT_SCRIPT,
                        help='Path to automation script')
    return parser.parse_args()


# ═══════════════════════════════════════════════════════════
# WORKER LAUNCHER
# ═══════════════════════════════════════════════════════════

def run_worker(config: dict, script_path: str) -> dict:
    """
    Launch a single worker as subprocess.
    Returns dict with worker_id, success, runtime, output_count
    """
    worker_id = config['worker_id']
    start_time = time.time()
    
    cmd = [
        sys.executable, 'worker_automation.py',
        '--worker-id', str(worker_id),
        '--cdp-port', str(config['cdp_port']),
        '--fs-port', str(config['file_server_port']),
        '--profile', config['chrome_profile'],
        '--output', config['output_dir'],
        '--start', str(config['prompt_start']),
        '--end', str(config['prompt_end']),
        '--script', script_path
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=False,  # Let output go to console
            timeout=4 * 3600  # 4 hour timeout
        )
        success = result.returncode == 0
    except subprocess.TimeoutExpired:
        success = False
    except Exception as e:
        print(f"[W{worker_id}] Error: {e}")
        success = False
    
    elapsed = time.time() - start_time
    
    # Count output files
    output_count = 0
    if os.path.exists(config['output_dir']):
        for root, dirs, files in os.walk(config['output_dir']):
            output_count += len(files)
    
    return {
        'worker_id': worker_id,
        'success': success,
        'runtime': elapsed,
        'output_count': output_count,
        'output_dir': config['output_dir']
    }


# ═══════════════════════════════════════════════════════════
# PROFILE SETUP
# ═══════════════════════════════════════════════════════════

def setup_profiles(configs: list):
    """
    Ensure Chrome profiles exist for all workers.
    If profile doesn't exist, shows login instructions.
    """
    missing_profiles = []
    
    for cfg in configs:
        profile_dir = cfg['chrome_profile']
        if not os.path.exists(profile_dir):
            missing_profiles.append(cfg)
    
    if missing_profiles:
        print("\n" + "=" * 60)
        print("  ⚠️  PROFILE SETUP REQUIRED")
        print("=" * 60)
        print("\nSome Chrome profiles don't exist yet.")
        print("You need to log into DeepSeek for each profile.\n")
        
        for cfg in missing_profiles:
            print(f"  Worker {cfg['worker_id']}: {cfg['chrome_profile']}")
        
        print("\n" + "-" * 60)
        print("Run these commands to set up each profile:")
        print("-" * 60 + "\n")
        
        for cfg in missing_profiles:
            print(f'# Worker {cfg["worker_id"]}:')
            print()
            print(f'# PowerShell:')
            print(f'Start-Process "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" -ArgumentList "--user-data-dir={cfg["chrome_profile"]}","--remote-debugging-port={cfg["cdp_port"]}","https://chat.deepseek.com"')
            print()
            print(f'# CMD:')
            print(f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --user-data-dir={cfg["chrome_profile"]} --remote-debugging-port={cfg["cdp_port"]} https://chat.deepseek.com')
            print()
        
        print("-" * 60)
        print("1. Run each command in a separate terminal")
        print("2. Log into DeepSeek in each Chrome window")
        print("3. Close the Chrome windows")
        print("4. Run this script again")
        print("-" * 60 + "\n")
        
        return False
    
    return True


# ═══════════════════════════════════════════════════════════
# OUTPUT MERGER
# ═══════════════════════════════════════════════════════════

def merge_outputs(worker_results: list, merged_dir: str):
    """
    Merge all worker outputs into a single directory.
    Preserves subdirectory structure.
    """
    print("\n" + "=" * 60)
    print("  MERGING OUTPUTS")
    print("=" * 60)
    
    os.makedirs(merged_dir, exist_ok=True)
    
    total_files = 0
    total_size = 0
    
    for result in worker_results:
        if not result['success']:
            print(f"  [W{result['worker_id']}] Skipped (failed)")
            continue
        
        src_dir = result['output_dir']
        if not os.path.exists(src_dir):
            continue
        
        worker_files = 0
        for root, dirs, files in os.walk(src_dir):
            for fname in files:
                src_path = os.path.join(root, fname)
                rel_path = os.path.relpath(src_path, src_dir)
                dst_path = os.path.join(merged_dir, rel_path)
                
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
                
                worker_files += 1
                total_size += os.path.getsize(src_path)
        
        total_files += worker_files
        print(f"  [W{result['worker_id']}] Merged {worker_files} files")
    
    print(f"\n  Total: {total_files} files ({total_size:,} bytes)")
    print(f"  Location: {merged_dir}")
    
    return total_files, total_size


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

async def run_parallel(configs: list, script_path: str):
    """Run all workers in parallel using subprocess"""
    print("\n" + "=" * 60)
    print("  LAUNCHING WORKERS")
    print("=" * 60 + "\n")
    
    # Launch all workers as separate processes
    processes = []
    for cfg in configs:
        cmd = [
            sys.executable, 'worker_automation.py',
            '--worker-id', str(cfg['worker_id']),
            '--cdp-port', str(cfg['cdp_port']),
            '--fs-port', str(cfg['file_server_port']),
            '--profile', cfg['chrome_profile'],
            '--output', cfg['output_dir'],
            '--start', str(cfg['prompt_start']),
            '--end', str(cfg['prompt_end']),
            '--script', script_path
        ]
        
        print(f"  Starting Worker {cfg['worker_id']}...")
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        processes.append((cfg, proc))
        
        # Stagger launches to avoid port conflicts
        await asyncio.sleep(3)
    
    print(f"\n  All {len(processes)} workers launched!")
    print("  Monitoring progress...\n")
    
    # Monitor all processes
    results = []
    start_time = time.time()
    
    while processes:
        for cfg, proc in processes[:]:
            retcode = proc.poll()
            
            # Read output without blocking
            try:
                line = proc.stdout.readline()
                if line:
                    print(line.rstrip())
            except:
                pass
            
            if retcode is not None:
                processes.remove((cfg, proc))
                
                # Count output files
                output_count = 0
                if os.path.exists(cfg['output_dir']):
                    for root, dirs, files in os.walk(cfg['output_dir']):
                        output_count += len(files)
                
                elapsed = time.time() - start_time
                results.append({
                    'worker_id': cfg['worker_id'],
                    'success': retcode == 0,
                    'runtime': elapsed,
                    'output_count': output_count,
                    'output_dir': cfg['output_dir']
                })
                
                status = "✅" if retcode == 0 else "❌"
                print(f"\n{status} Worker {cfg['worker_id']} finished (code: {retcode})")
        
        await asyncio.sleep(1)
    
    return results


def main():
    args = parse_args()
    
    print("=" * 60)
    print("  DeepSeek Parallel Automation")
    print("=" * 60)
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Workers: {args.workers}")
    print(f"  Total prompts: {PROMPT_COUNT}")
    print(f"  Script: {args.script}")
    print()
    
    # Validate config
    errors = validate_config()
    if errors:
        print("⚠️  Configuration errors:")
        for e in errors:
            print(f"  - {e}")
        return 1
    
    # Get worker configs
    from parallel_config import get_all_worker_configs
    configs = get_all_worker_configs(args.workers)
    
    # Display worker assignments
    print("  Worker Assignments:")
    print("  " + "-" * 50)
    for cfg in configs:
        print(f"    W{cfg['worker_id']}: Prompts {cfg['prompt_start']:2d}-{cfg['prompt_end']:2d} "
              f"| CDP:{cfg['cdp_port']} FS:{cfg['file_server_port']}")
    print()
    
    # Dry run mode
    if args.dry_run:
        print("  [DRY RUN] No workers will be started.")
        print()
        print("  Chrome profiles needed:")
        for cfg in configs:
            exists = "✓" if os.path.exists(cfg['chrome_profile']) else "✗ (missing)"
            print(f"    {cfg['chrome_profile']} {exists}")
        print()
        print("  Output directories:")
        for cfg in configs:
            print(f"    {cfg['output_dir']}")
        if MERGE_OUTPUTS and not args.no_merge:
            print(f"    → {MERGED_OUTPUT_DIR} (merged)")
        return 0
    
    # Check profiles exist
    if not setup_profiles(configs):
        return 1
    
    # Verify script exists
    if not os.path.exists(args.script):
        print(f"❌ Script not found: {args.script}")
        print("   Run: python build_template.py")
        return 1
    
    # Create output directories
    for cfg in configs:
        os.makedirs(cfg['output_dir'], exist_ok=True)
    
    # Run workers
    start_time = time.time()
    
    if args.sequential:
        print("\n  [SEQUENTIAL MODE] Running workers one at a time...")
        results = []
        for cfg in configs:
            result = run_worker(cfg, args.script)
            results.append(result)
    else:
        results = asyncio.run(run_parallel(configs, args.script))
    
    total_time = time.time() - start_time
    
    # Summary
    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    
    total_success = sum(1 for r in results if r['success'])
    total_files = sum(r['output_count'] for r in results)
    
    for r in results:
        status = "✅" if r['success'] else "❌"
        print(f"  {status} Worker {r['worker_id']}: {r['output_count']} files")
    
    print()
    print(f"  Workers: {total_success}/{len(results)} successful")
    print(f"  Files: {total_files} total")
    print(f"  Time: {int(total_time // 60)}m {int(total_time % 60)}s")
    
    # Merge outputs
    if MERGE_OUTPUTS and not args.no_merge and total_files > 0:
        merge_outputs(results, MERGED_OUTPUT_DIR)
    
    print("\n" + "=" * 60)
    
    return 0 if total_success == len(results) else 1


# ═══════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n  Interrupted by user")
        print("  Note: Worker processes may still be running.")
        print("  Use Task Manager to close Chrome instances if needed.")
        sys.exit(1)
    except Exception as e:
        print(f"\n  Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
