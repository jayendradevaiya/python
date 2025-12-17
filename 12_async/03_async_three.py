import asyncio
import aiohttp

async def fatch_url(session, url):
    async with session.get(url) as response:
        print(f"Fatched {url} with satus {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] *3
    async with aiohttp.ClientSession() as session:
        tasks = [fatch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())