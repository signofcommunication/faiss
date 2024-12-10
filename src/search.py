import faiss

def create_index(embeddings):
    embedding_dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(embeddings)
    return index

def save_index(index,file_path):
    faiss.write_index(index, file_path)

def load_index(file_path):
    return faiss.read_index(file_path)

def search_index(index,query_embedding, k = 5):
    distances, indices = index.search(query_embedding, k)
    return distances, indices