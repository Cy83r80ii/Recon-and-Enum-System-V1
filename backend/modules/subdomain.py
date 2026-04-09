import requests

SUBDOMAIN_WORDLIST = [
    "api",
    "dev",
    "admin",
    "test",
    "staging",
    "internal",
    "beta"
]


def scan_subdomains(target):

    findings = []

    try:

        domain = target.split("//")[-1].split("/")[0]

        for sub in SUBDOMAIN_WORDLIST:

            url = f"http://{sub}.{domain}"

            try:

                r = requests.get(url, timeout=3)

                if r.status_code < 500:

                    findings.append({
                        "type": "subdomain",
                        "url": url,
                        "severity": "info"
                    })

            except:
                pass

    except:
        pass

    return findings
