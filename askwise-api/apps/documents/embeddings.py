# apps/documents/embeddings.py
from sentence_transformers import SentenceTransformer
_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: list[str]) -> list[list[float]]:
    """
        Generate a 384-dimensional embedding for the given text using the 
        'all-MiniLM-L6-v2' model from SentenceTransformers.
    """
    
    return _model.encode(text).tolist()

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
        Generate embeddings for a list of texts using the 'all-MiniLM-L6-v2' model.
    """
    
    return _model.encode(texts).tolist( )