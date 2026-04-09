import aiohttp
import asyncio

SESSION = None


async def get_session():

    global SESSION

    if SESSION is None:
        timeout = aiohttp.ClientTimeout(total=20)

        connector = aiohttp.TCPConnector(
            limit=100,
            limit_per_host=20,
            ssl=False
        )

        SESSION = aiohttp.ClientSession(
            timeout=timeout,
            connector=connector
        )

    return SESSION


async def fetch(url):

    session = await get_session()

    try:

        async with session.get(url) as resp:

            text = await resp.text()

            return {
                "url": url,
                "status": resp.status,
                "body": text,
                "length": len(text)
            }

    except:
        return None
