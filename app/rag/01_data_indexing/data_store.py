# data_store.py

class DataStore:
    def store_embeddings(self, embeddings):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

import pinecone

class PineconeDataStore(DataStore):
    def __init__(self, api_key, environment, index_name):
        pinecone.init(api_key=api_key, environment=environment)
        self.index_name = index_name
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name, dimension=1536)
        self.index = pinecone.Index(index_name)

    def store_embeddings(self, embeddings):
        vectors = []
        for i, item in enumerate(embeddings):
            vectors.append((str(i), item['embedding'], {'text': item['text']}))
        self.index.upsert(vectors)