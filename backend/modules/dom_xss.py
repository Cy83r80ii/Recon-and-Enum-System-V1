import requests


SOURCES = [
    "document.location",
    "document.URL",
    "location.hash",
    "location.search"
]

SINKS = [
    "innerHTML",
    "document.write",
    "eval(",
    "setTimeout("
]


def scan_dom_xss(urls):

    findings = []

    for url in urls:

        try:

            r = requests.get(url, timeout=5)

            js = r.text

            for src in SOURCES:
                for sink in SINKS:

                    if src in js and sink in js:

                        findings.append({
                            "type": "DOM XSS",
                            "url": url,
                            "severity": "medium"
                        })

        except:
            pass

    return findings
