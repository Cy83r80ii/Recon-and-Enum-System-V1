from utils.http import session, TIMEOUT


def scan_wordpress(target):

    findings = []

    try:

        r = session.get(target + "/wp-login.php", timeout=TIMEOUT)

        if "wordpress" in r.text.lower():

            findings.append({
                "type": "WordPress Detected",
                "severity": "info",
                "url": target
            })

    except:
        pass

    return findings
