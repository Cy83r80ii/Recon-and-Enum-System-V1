import asyncio
import time

from utils.payload_mutator import mutate_payloads
from utils.response_analyzer import analyze_response
from utils.http_client import fetch


ERROR_PATTERNS = [
    "sql syntax",
    "mysql",
    "warning: mysql",
    "unclosed quotation mark",
    "syntax error",
    "pdoexception",
    "database error"
]


async def test_sqli(url, param):

    findings = []

    payloads = mutate_payloads()

    # baseline request
    baseline_resp = await fetch(url)

    if not baseline_resp:
        return findings

    baseline = baseline_resp["body"]

    for payload in payloads:

        attack_url = f"{url}&{param}={payload}"

        try:

            start = time.time()

            resp = await fetch(attack_url)

            if not resp:
                continue

            injected = resp["body"]

            delay = time.time() - start

            # Error-based SQLi
            for err in ERROR_PATTERNS:

                if err in injected.lower():

                    findings.append({
                        "type": "SQL Injection",
                        "technique": "error-based",
                        "url": attack_url,
                        "param": param,
                        "severity": "high"
                    })

            # Response diff detection
            if analyze_response(baseline, injected):

                findings.append({
                    "type": "SQL Injection",
                    "technique": "response-diff",
                    "url": attack_url,
                    "param": param,
                    "severity": "medium"
                })

            # Time-based detection
            if delay > 5:

                findings.append({
                    "type": "SQL Injection",
                    "technique": "time-based",
                    "url": attack_url,
                    "param": param,
                    "severity": "high"
                })

        except:
            pass

    return findings


async def scan_sqli(params):

    tasks = []

    for item in params:

        url = item["url"]
        param = item["param"]

        tasks.append(test_sqli(url, param))

    results = await asyncio.gather(*tasks)

    findings = []

    for r in results:
        findings.extend(r)

    return findings
