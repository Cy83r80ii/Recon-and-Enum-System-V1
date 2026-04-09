import requests

WAF_SIGNATURES = [
    "cloudflare",
    "sucuri",
    "incapsula",
    "akamai",
    "mod_security",
    "f5 big-ip"
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
                    "type": "WAF",
                    "name": waf,
                    "url": target,
                    "severity": "info"
                })

    except:
        pass

    return findings
