import asyncio
import aiohttp


async def dispatch_requests(urls, concurrency=80):

    results = []

    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:

        async def worker(url):

            async with semaphore:

                try:

                    async with session.get(url, timeout=10) as resp:

                        text = await resp.text()

                        results.append({
                            "url": url,
                            "status": resp.status,
                            "length": len(text)
                        })

                except:
                    pass

        tasks = [worker(u) for u in urls]

        await asyncio.gather(*tasks)

    return results
