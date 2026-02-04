import asyncio, json, sys, urllib.request
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

async def check():
    import websockets
    with urllib.request.urlopen("http://localhost:9222/json") as r:
        tabs = json.loads(r.read())
    tab = next(t for t in tabs if "deepseek" in t.get("url",""))
    async with websockets.connect(tab["webSocketDebuggerUrl"], max_size=None) as ws:
        await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":"FIGMA_AUTO.status()","returnByValue":True}}))
        resp = json.loads(await ws.recv())
        val = resp.get("result",{}).get("result",{}).get("value","")
        status = json.loads(val) if isinstance(val, str) else val
        print(f"Running: {status['running']}")
        print(f"Prompt: {status['nextPromptId']}/{status['totalPrompts']}")
        print(f"Exported: {status['totalExported']}")
        print(f"Parts: {status['totalParts']}")
        print(f"Folder: {status['folderName']} (ready: {status['folderReady']})")
        print(f"\nRecent log:")
        for line in status['log'][-8:]:
            print(f"  {line}")

asyncio.run(check())
