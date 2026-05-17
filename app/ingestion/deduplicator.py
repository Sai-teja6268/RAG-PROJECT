from typing import Any, Iterable, List


def deduplicate_documents(documents: Iterable[Any]) -> List[Any]:
    """Remove duplicate documents by page content."""
    seen: set[str] = set()
    unique_documents: List[Any] = []

    for document in documents:
        content = getattr(document, "page_content", str(document))
        if content in seen:
            continue
        seen.add(content)
        unique_documents.append(document)

    return unique_documents

