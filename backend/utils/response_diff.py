def response_diff(original, injected):

    if not original or not injected:
        return False

    if len(original) != len(injected):
        return True

    if original != injected:
        return True

    return False
