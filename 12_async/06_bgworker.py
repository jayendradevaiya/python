import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Loogging the system health 🍵")

async def fatch_orders():
    await asyncio.sleep(3)
    print("🎁 order fatched")


threading.Thread(target=background_worker,daemon=True).start()
asyncio.run(fatch_orders())