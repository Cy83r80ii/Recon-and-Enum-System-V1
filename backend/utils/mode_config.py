def get_mode_config(mode: str):
    if mode == "deep":
        return {
            "sql_level": "5",
            "sql_risk": "3",
            "max_targets": 10,
            "nuclei_severity": "low,medium,high,critical"
        }
    else:  # fast
        return {
            "sql_level": "1",
            "sql_risk": "1",
            "max_targets": 3,
            "nuclei_severity": "high,critical"
        }
