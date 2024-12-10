from sentence_transformers import SentenceTransformers
import numpy as np

def load_model(model_name='all-MiniLM-L6-v2'):
    return SentenceTransformers(model_name)

def generate_embeddings(model,text):
    return np.array([model.encode(text) for text in texts])

