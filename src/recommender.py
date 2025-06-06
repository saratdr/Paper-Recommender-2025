import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_metadata, load_all_embeddings, get_PDF_URL, normalize_text

class Recommender:
    def __init__(self):
        self.models = {}
        self.metadata = load_metadata()
        self.models = load_all_embeddings()

    def recommend(self, model, query, encoder, top_k=5):
        if model not in self.models:
            raise ValueError(f"Model '{model}' not found. Available models: {list(self.models.keys())}")

        embeddings = self.models[model]
        metadata = self.metadata
        
        query_clean = normalize_text(query.strip().lower())

        # STEP 1: Try exact title match
        exact_match = metadata[metadata['title'].apply(normalize_text) == query_clean]

        if not exact_match.empty:
            anchor_idx = exact_match.index[0]
            anchor_vector = embeddings[anchor_idx].reshape(1, -1)
        
        # STEP 2: Fall back to embedding the query
        else:
            anchor_vector = encoder.encode(query, model).reshape(1, -1)

        # STEP 3: Compute cosine similarity
        sims = cosine_similarity(anchor_vector, embeddings).flatten()
        top_indices = np.argsort(sims)[-top_k:][::-1]

        results = []

        for idx in top_indices:
            row = metadata.iloc[idx]
            results.append({
                'id': row['id'],
                'title': row['title'],
                'abstract': row['abstract'],
                'authors': row['authors'],
                'date': row['update_date'],
                'doi': row['doi'],
                'categories': row['categories'],
                'main_category': row['main_category'],
                'similarity': round(sims[idx], 3),
                'pdf_url': get_PDF_URL(row['id'])
            })
        
        return results
