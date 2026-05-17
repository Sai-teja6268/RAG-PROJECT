def estimate_confidence(contexts: list[dict]) -> float:
    return 0.0 if not contexts else 1.0 / (1.0 + float(contexts[0].get("distance", 0.0)))

