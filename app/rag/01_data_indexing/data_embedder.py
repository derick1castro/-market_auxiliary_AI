import logging
from langchain_openai import OpenAIEmbeddings

logging.basicConfig(level=logging.INFO)
#client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

class DataEmbedder:
    def embed_data(self, chunks):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class OpenAIDataEmbedder(DataEmbedder):
    def __init__(self):
        pass
    
    def embedding_data(self, chunks):
        
        embedding = OpenAIEmbeddings().embed_documents([doc.page_content for doc in chunks])

        # response = client.embeddings.create(
        #     input=chunks,
        #     model="text-embedding-3-small"
        # )
        # embedding = response.data[0].embedding
        
        return embedding
    
