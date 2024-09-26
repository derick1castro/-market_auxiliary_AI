# data_indexer.py

class DataIndexer:
    def __init__(self, loader, splitter, embedder, store):
        self.loader = loader
        self.splitter = splitter
        self.embedder = embedder
        self.store = store

    def index_data(self):
        data = self.loader.load_data()
        chunks = self.splitter.split_data(data)
        embeddings = self.embedder.embed_data(chunks)
        self.store.store_embeddings(embeddings)
