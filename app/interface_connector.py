from src.recommender import Recommender
from src.encoder import QueryEncoder

recommender = Recommender()
encoder = QueryEncoder()

def get_recommendations(query, model, top_k=5):
    """
    Get recommendations based on the query and model.
    
    :param query: The search query string.
    :param model: The model name to use for recommendations.
    :param top_k: The number of top recommendations to return.
    :return: A list of recommended papers with their metadata.
    """
    if model not in recommender.models:
        raise ValueError(f"Model '{model}' not found. Available models: {list(recommender.models.keys())}")

    return recommender.recommend(model, query, encoder, top_k)