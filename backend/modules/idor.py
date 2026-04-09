from utils.http import session, TIMEOUT


def scan_idor(params):

    findings = []

    for item in params:

        url = item["url"]
        param = item["param"]

        for i in range(1,10):

            test = f"{url}?{param}={i}"

            try:

                r = session.get(test, timeout=TIMEOUT)

                if "user" in r.text.lower():

                    findings.append({
                        "type": "IDOR",
                        "severity": "high",
                        "url": test
                    })

            except:
                pass

    return findings
