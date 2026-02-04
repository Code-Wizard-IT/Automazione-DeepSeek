"""
Quick-check: verifica che tutti i file dell'automazione DeepSeek esistano.
Usato da Claude per verificare prima di lanciare launch_automation.py
"""
import os
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

files = {
    'Build script': r'C:\Users\cresc\Desktop\build_script_v2.py',
    'Generated script': r'C:\Users\cresc\Desktop\figma-deepseek-automation-v2.1.user.js',
    'CDP Launcher': r'C:\Users\cresc\Desktop\launch_chrome_cdp.bat',
    'CDP Injector': r'C:\Users\cresc\Desktop\launch_automation.py',
    'Prompts folder': r'C:\Users\cresc\Desktop\Prompt',
}

all_ok = True
for name, path in files.items():
    exists = os.path.exists(path)
    status = "✅" if exists else "❌"
    size = ""
    if exists and os.path.isfile(path):
        size = f" ({os.path.getsize(path):,} bytes)"
    print(f"  {status} {name}: {path}{size}")
    if not exists:
        all_ok = False

if all_ok:
    print("\n✅ Tutto pronto. Esegui: python launch_automation.py")
else:
    print("\n❌ File mancanti. Ricostruisci con build_script_v2.py")
