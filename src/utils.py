from config import METADATA_PATH, EMBEDDINGS_PATHS
import pandas as pd
import numpy as np
import re

def clean_text(text):
    """
    Clean a text string by removing newlines and normalizing whitespace.
    
    Args:
        text (str): Input string
    Returns:
        str: Cleaned string
    """
    text = re.sub(r"\\n", " ", text)      # replace literal '\n' (escaped in CSV)
    text = re.sub(r"\n", " ", text)       # replace real newlines (if any)
    text = re.sub(r"\s+", " ", text)      # normalize whitespace
    return text.strip()

def clean_text_column(series):
    return series.astype(str).apply(clean_text)

def load_metadata():
    """Load metadata from the CSV file."""
    metadata = pd.read_csv(METADATA_PATH)
    metadata['title'] = clean_text_column(metadata['title'])
    return metadata

def load_embeddings(model_name):
    """Load embeddings for a specific model."""
    if model_name not in EMBEDDINGS_PATHS:
        raise ValueError(f"Model '{model_name}' not found in data paths.")
    return np.load(EMBEDDINGS_PATHS[model_name]) if model_name in EMBEDDINGS_PATHS else None

def load_all_embeddings():
    """Load all embeddings for all models."""
    embeddings = {}
    for model_name in EMBEDDINGS_PATHS:
        embeddings[model_name] = load_embeddings(model_name)
    return embeddings

def get_PDF_URL(arxiv_id):
    """Construct the PDF URL for a given arXiv ID."""
    base_url = "https://arxiv.org/pdf/"
    return f"{base_url}{arxiv_id}.pdf"

def process_user_input(user_input: str):
    """Process user input to extract keywords or phrases."""
    user_input = user_input.strip().lower()    
    if ',' in user_input:
        keywords = [kw.strip() for kw in user_input.split(',') if kw.strip()]
    else:
        keywords = [user_input]
        
    return keywords

def normalize_text(text):
    """Normalize text by converting to lowercase, removing non-alphanumeric characters, and collapsing whitespace."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # remove non-alphanumeric chars
    text = re.sub(r'\s+', ' ', text)         # collapse whitespace
    return text.strip()