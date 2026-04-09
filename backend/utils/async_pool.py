import aiohttp
import asyncio

# maximum parallel requests
MAX_CONCURRENT = 50

semaphore = asyncio.Semaphore(MAX_CONCURRENT)


async def fetch(session, url):

    try:
        async with semaphore:

            async with session.get(url, timeout=10) as response:

                text = await response.text()

                return {
                    "url": url,
                    "status": response.status,
                    "text": text
                }

    except Exception:

        return None


async def request_pool(urls):

    results = []

    async with aiohttp.ClientSession() as session:

        tasks = [fetch(session, u) for u in urls]

        responses = await asyncio.gather(*tasks)

        for r in responses:
            if r:
                results.append(r)

    return results
