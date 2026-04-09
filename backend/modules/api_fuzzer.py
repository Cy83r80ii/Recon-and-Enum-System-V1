import requests

API_PATHS = [
    "/api",
    "/api/v1",
    "/api/v2",
    "/graphql",
    "/swagger.json",
    "/openapi.json",
    "/auth/login",
    "/auth/register",
    "/users",
    "/admin/api"
]


def scan_api(target):

    findings = []

    base = target.rstrip("/")

    for path in API_PATHS:

        url = base + path

        try:

            r = requests.get(url, timeout=5)

            if r.status_code in [200, 401, 403]:

                findings.append({
                    "type": "API Endpoint",
                    "url": url,
                    "status": r.status_code,
                    "severity": "info"
                })

        except:
            pass

    return findings
