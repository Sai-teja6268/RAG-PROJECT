from sentence_transformers import SentenceTransformer

from app.core.constants import DEFAULT_EMBEDDING_MODEL

_model_cache = {}

def load_embedding_model(model_name: str = DEFAULT_EMBEDDING_MODEL) -> SentenceTransformer:
    if model_name not in _model_cache:
        logger.info(
            f"Loading embedding model: {model_name}"
        )
        _model_cache[model_name] = SentenceTransformer(model_name)
    
    logger.info(
        f"Embedding model {model_name} is already loaded."
    )
    return _model_cache[model_name]


