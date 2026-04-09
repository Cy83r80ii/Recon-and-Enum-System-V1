import requests

def check_wordpress(url):
    try:
        r = requests.get(url, timeout=5)
        if "wp-content" in r.text or "wp-admin" in r.text:
            return {
                "type": "WordPress Detected",
                "endpoint": url,
                "method": "GET",
                "confidence": 70,
                "description": "WordPress CMS detected"
            }
    except:
        pass
    return None
