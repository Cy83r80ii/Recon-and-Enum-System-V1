import subprocess
import json


def run_nuclei(target):

    findings = []

    try:

        result = subprocess.run(
            ["nuclei", "-u", target, "-json"],
            capture_output=True,
            text=True
        )

        for line in result.stdout.splitlines():

            data = json.loads(line)

            findings.append({
                "type": "nuclei",
                "template": data.get("template-id"),
                "severity": data.get("severity"),
                "url": data.get("matched-at")
            })

    except:
        pass

    return findings
