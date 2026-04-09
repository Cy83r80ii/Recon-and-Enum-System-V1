import subprocess
import json


def run_wpscan(url: str):
    """
    Safe WPScan runner.
    Requires wpscan installed and accessible.
    """

    cmd = [
        "wpscan",
        "--url", url,
        "--format", "json",
        "--no-update"
    ]

    try:
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )

        if not process.stdout:
            return None

        data = json.loads(process.stdout)

        if data.get("vulnerabilities") or data.get("version", {}).get("vulnerabilities"):
            return {
                "type": "WordPress Vulnerability",
                "engine": "wpscan",
                "url": url,
                "confidence": 85,
                "score": 6
            }

    except subprocess.TimeoutExpired:
        return None
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    except Exception:
        return None

    return None
