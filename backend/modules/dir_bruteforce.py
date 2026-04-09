import requests

COMMON_DIRS = [
    "admin",
    "login",
    "dashboard",
    ".git",
    ".env",
    "backup",
    "backup.zip",
    "api",
    "dev",
    "staging",
    "test"
]


def scan_directories(target):

    findings = []

    for d in COMMON_DIRS:

        url = f"{target.rstrip('/')}/{d}"

        try:

            r = requests.get(url, timeout=5)

            if r.status_code in [200, 401, 403]:

                findings.append({
                    "type": "directory",
                    "url": url,
                    "status": r.status_code,
                    "severity": "info"
                })

        except:
            pass

    return findings
