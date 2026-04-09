import subprocess
import re


def run_sqlmap(url: str, mode: str = "fast"):
    """
    Safe, non-interactive sqlmap runner.
    Timeout protected.
    Returns structured result or None.
    """

    level = "1" if mode == "fast" else "3"
    risk = "1" if mode == "fast" else "2"
    timeout_value = 60 if mode == "fast" else 150

    cmd = [
        "sqlmap",
        "-u", url,
        "--batch",
        "--level", level,
        "--risk", risk,
        "--random-agent",
        "--flush-session",
        "--answers=follow=Y"
    ]

    try:
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_value
        )

        output = process.stdout.lower()

        if "injectable" in output or "is vulnerable" in output:

            injection_types = re.findall(r"type:\s*(.+)", output)
            dbms_match = re.search(r"back-end dbms:\s*(.+)", output)

            return {
                "type": "SQL Injection",
                "engine": "sqlmap",
                "url": url,
                "injection_types": injection_types if injection_types else [],
                "dbms": dbms_match.group(1) if dbms_match else "Unknown",
                "confidence": 95 if mode == "deep" else 85,
                "score": 9
            }

    except subprocess.TimeoutExpired:
        return None
    except FileNotFoundError:
        return None
    except Exception:
        return None

    return None
