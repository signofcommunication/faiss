import numpy as np
from src.preprocess import load_data, preprocess_data
from src.embeddings import load_model,generate_embeddings
from src.search import create_index,search_index

data_file = 'data/data.csv'
df = load_data(data_file)
df = preprocess_data(df)

model = load_model()

df['embeddings'] = generate_embeddings(model,df['description'])
embeddings = np.array(df['embeddings'].tolist())

index = create_index(embeddings)

query = 'eco-friendly-product'
query_embedding = model.encode(query).reshape(1,-1)
distances,indices = search_index(index,query_embedding,k=5)

print("Hasil Pencarian : ")
for idx in indices[0]:
    print(df.iloc[idx]['title'],"-", df.iloc[idx]['description'])