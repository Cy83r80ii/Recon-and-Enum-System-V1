import requests

session = requests.Session()

session.headers.update({
    "User-Agent": "ARES-X Security Scanner",
    "Accept": "*/*",
    "Connection": "keep-alive"
})

TIMEOUT = 3
