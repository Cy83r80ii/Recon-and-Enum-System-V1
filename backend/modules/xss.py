import aiohttp
import asyncio
from utils.payload_mutator import mutate_payloads


async def test_xss(session, url, param):

    findings = []

    payloads = mutate_payloads()

    for payload in payloads:

        attack = f"{url}&{param}={payload}"

        try:

            async with session.get(attack, timeout=10) as resp:

                text = await resp.text()

                if payload in text:

                    findings.append({
                        "type": "XSS",
                        "technique": "reflected",
                        "url": attack,
                        "param": param,
                        "severity": "medium"
                    })

        except:
            pass

    return findings


async def scan_xss(params):

    findings = []

    async with aiohttp.ClientSession() as session:

        tasks = []

        for item in params:

            tasks.append(
                test_xss(session, item["url"], item["param"])
            )

        results = await asyncio.gather(*tasks)

        for r in results:
            findings.extend(r)

    return findings
