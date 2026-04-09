def calculate_severity(score: int) -> str:
    """
    Converts numeric score into severity label.
    """

    if score >= 9:
        return "Critical"
    elif score >= 7:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"
