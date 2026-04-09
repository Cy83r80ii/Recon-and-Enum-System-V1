import asyncio


async def run_tasks(tasks, concurrency=80):

    semaphore = asyncio.Semaphore(concurrency)

    async def wrapper(task):

        async with semaphore:
            return await task

    wrapped = [wrapper(t) for t in tasks]

    return await asyncio.gather(*wrapped)
