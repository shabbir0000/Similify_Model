import re
import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv("data/cleaned_news.xls")

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

# -------------------------
# FastAPI App
# -------------------------

app = FastAPI(title="News Duplicate Detection API")

# -------------------------
# Cleaning Function
# -------------------------

def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\b[a-z]\b", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text

# -------------------------
# Request Model
# -------------------------

class ArticleRequest(BaseModel):
    text: str
    top_n: int = 5

# -------------------------
# Endpoint
# -------------------------

@app.post("/find_similar")
def find_similar_articles(request: ArticleRequest):

    cleaned_text = clean_text(request.text)

    new_vector = vectorizer.transform([cleaned_text])

    similarity_scores = cosine_similarity(new_vector, tfidf_matrix)[0]

    top_indices = np.argsort(similarity_scores)[::-1][:request.top_n]

    results = df.loc[top_indices, [
        "article_id",
        "title",
        "url",
        "published_at",
        "url_to_image",
        "category",
        "author",
        "source_name"
    ]].copy()

    results["similarity_score"] = similarity_scores[top_indices]
    results = results.replace({np.nan: None})
    duplicate_threshold = 0.40  # 🔥 your chosen threshold
    is_duplicate = any(results["similarity_score"] >= duplicate_threshold)

    return {
        "is_duplicate": bool(is_duplicate),
        "results": results.to_dict(orient="records")
    }