from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(user_text: str, model_text: str) -> float:
    user_emb = _model.encode([user_text])
    model_emb = _model.encode([model_text])

    return float(cosine_similarity(user_emb, model_emb)[0][0])