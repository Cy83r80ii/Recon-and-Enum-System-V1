def analyze_response(baseline, injected):

    if baseline is None or injected is None:
        return False

    # length change
    if abs(len(baseline) - len(injected)) > 20:
        return True

    # content change
    if baseline != injected:
        return True

    return False
