from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer, AutoModel

class QueryEncoder:
    def __init__(self):
        self.models = {
            "minilm": SentenceTransformer("all-MiniLM-L6-v2"),
            "specter": self._load_model("allenai/specter"),
            "scibert": self._load_model("allenai/scibert_scivocab_uncased")
        }

        self.tokenizers = {
            "specter": AutoTokenizer.from_pretrained("allenai/specter"),
            "scibert": AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        }

    def _load_model(self, model_name):
        return AutoModel.from_pretrained(model_name)

    def encode(self, text, model):
        if model == "minilm":
            return self.models[model].encode(text)
        
        tokenizer = self.tokenizers[model]
        model = self.models[model]
        tokens = tokenizer(text, return_tensors='pt', truncation=True, max_length=512, padding="max_length")

        with torch.no_grad():
            outputs = model(**tokens)
            cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze().numpy()
        return cls_embedding