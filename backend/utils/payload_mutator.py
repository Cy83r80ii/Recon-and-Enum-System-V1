BASE_PAYLOADS = [
    "'",
    "\"",
    "<script>alert(1)</script>",
    "' OR 1=1--"
]


def mutate_payloads():

    mutated = []

    for p in BASE_PAYLOADS:

        mutated.append(p)
        mutated.append(p + "--")
        mutated.append(p + "#")
        mutated.append(p + "/*")
        mutated.append(p + "'")

    return list(set(mutated))
