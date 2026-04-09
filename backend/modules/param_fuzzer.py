import requests

COMMON_PARAMS = [
    "id",
    "user",
    "username",
    "file",
    "page",
    "redirect",
    "url",
    "next",
    "data",
    "path"
]

def fuzz_params(urls):

    findings = []

    for url in urls[:25]:

        for param in COMMON_PARAMS:

            attack = f"{url}?{param}=1"

            try:

                r = requests.get(
                    attack,
                    timeout=2   # faster timeout
                )

                if r.status_code == 200:

                    findings.append({
                        "type": "parameter",
                        "url": attack,
                        "severity": "info"
                    })

            except:
                pass

    return findings
