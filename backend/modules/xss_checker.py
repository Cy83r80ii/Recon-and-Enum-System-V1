import requests


def check_xss(url):

    payloads = [
        "<script>alert(1)</script>",
        "'\"><img src=x onerror=alert(1)>"
    ]

    findings = []

    for payload in payloads:
        try:
            test_url = url + payload
            r = requests.get(test_url, timeout=5)

            if payload in r.text:
                findings.append({
                    "type": "Reflected XSS",
                    "url": url,
                    "payload": payload,
                    "confidence": 75
                })
        except:
            continue

    return findings if findings else None
