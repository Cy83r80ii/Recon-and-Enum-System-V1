import requests

WAF_SIGNATURES = [
    "cloudflare",
    "sucuri",
    "incapsula",
    "akamai",
    "f5 big-ip",
    "mod_security"
]


def detect_waf(target):

    findings = []

    try:

        r = requests.get(target, timeout=5)

        headers = str(r.headers).lower()
        body = r.text.lower()

        for waf in WAF_SIGNATURES:

            if waf in headers or waf in body:

                findings.append({
                    "type": "WAF Detected",
                    "name": waf,
                    "severity": "info"
                })

    except:
        pass

    return findings
