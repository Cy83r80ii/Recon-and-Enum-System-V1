import asyncio
import aiohttp


async def batch_requests(urls, concurrency=50):

    results = []

    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:

        async def fetch(url):

            async with semaphore:

                try:
                    async with session.get(url) as r:
                        text = await r.text()
                        results.append((url, r.status, len(text)))
                except:
                    pass

        tasks = [fetch(u) for u in urls]

        await asyncio.gather(*tasks)

    return results
