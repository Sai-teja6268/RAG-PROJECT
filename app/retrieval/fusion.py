def reciprocal_rank_fusion(result_sets, k: int = 60):
    """Combine ranked result sets with reciprocal rank fusion."""
    scores = {}
    items = {}
    for results in result_sets:
        for rank, item in enumerate(results, start=1):
            key = item.get("page_content", repr(item))
            scores[key] = scores.get(key, 0.0) + 1.0 / (k + rank)
            items[key] = item
    return [items[key] for key, _ in sorted(scores.items(), key=lambda pair: pair[1], reverse=True)]

