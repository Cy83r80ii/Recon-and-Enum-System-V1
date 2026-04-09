import requests

COMMON_PATHS = [
    "/admin",
    "/login",
    "/dashboard",
    "/config",
    "/backup"
]


def discover_directories(base_url):

    found = []

    for path in COMMON_PATHS:
        try:
            r = requests.get(base_url.rstrip("/") + path, timeout=5)
            if r.status_code < 400:
                found.append(base_url.rstrip("/") + path)
        except:
            continue

    return found
