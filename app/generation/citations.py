def build_citations(contexts: list[dict]) -> list[dict]:
    return [context.get("metadata", {}) for context in contexts]

