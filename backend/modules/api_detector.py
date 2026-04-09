import requests

API_ENDPOINTS = [
    "/graphql",
    "/swagger.json",
    "/openapi.json",
    "/api-docs"
]


def detect_api(target):

    findings = []

    base = target.rstrip("/")

    for ep in API_ENDPOINTS:

        url = base + ep

        try:

            r = requests.get(url, timeout=5)

            if r.status_code == 200:

                findings.append({
                    "type": "API Documentation",
                    "url": url,
                    "severity": "medium"
                })

        except:
            pass

    return findings
