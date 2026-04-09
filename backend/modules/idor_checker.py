import requests
import re


def check_idor(url):

    match = re.search(r"(id=)(\d+)", url)
    if not match:
        return None

    current_id = int(match.group(2))
    test_url = url.replace(f"id={current_id}", f"id={current_id + 1}")

    try:
        r1 = requests.get(url, timeout=5)
        r2 = requests.get(test_url, timeout=5)

        if r1.status_code == 200 and r2.status_code == 200:
            if len(r1.text) != len(r2.text):
                return {
                    "type": "Possible IDOR",
                    "url": test_url,
                    "confidence": 60
                }
    except:
        pass

    return None
