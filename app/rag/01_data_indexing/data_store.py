import os
import sys
import pinecone
from pinecone import ServerlessSpec
from langchain.vectorstores import Pinecone
from loguru import logger

# Ajusta o sys.path para garantir que a pasta 'rag' seja encontrada
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o arquivo config do projeto
from config import config

class DataStore:
    """
    Classe base abstrata para armazenar embeddings. Subclasses devem implementar o método store_embeddings.
    """
    def store_embeddings(self, embeddings):
        """
        Método abstrato para armazenar embeddings.

        Args:
        - embeddings (list): Lista de embeddings a serem armazenados.

        Raises:
        - NotImplementedError: Se o método não for implementado por uma subclasse.
        """
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class PineconeDataStore(DataStore):
    """
    Classe responsável por armazenar embeddings no banco de dados vetorial Pinecone.
    """
    def __init__(self, index_name):
        """
        Inicializa a classe PineconeDataStore e configura o índice no Pinecone.

        Args:
        - index_name (str): Nome do índice no Pinecone onde os embeddings serão armazenados.
        """
        self.index_name = index_name

        # Inicializa a conexão com o Pinecone usando a chave da API
        pc = pinecone.Pinecone(api_key=config.PINECONE_API_KEY)

        # Verifica se o índice já existe, senão cria um novo
        if self.index_name not in pc.list_indexes().names():
            logger.info(f'Criando o índice: {index_name}')
            pc.create_index(
                name=self.index_name,
                dimension=config.DIMENSION,
                metric=config.METRIC,
                spec=ServerlessSpec(
                    cloud=config.CLOUD_PROVIDER,
                    region=config.REGION
                )
            )
            logger.success('Índice criado com sucesso!')
        else:
            logger.info(f'Índice {self.index_name} já existe.')

        # Deletar um Index no Data Vector Pinecone
        # if self.index_name in pc.list_indexes().names():
        #     print(f'Deleting index {self.index_name} ... ')
        #     pc.delete_index(self.index_name)
        #     print('Done!')
        # else:
        #     print(f'Index {self.index_name} does not exist!')

    def store_embeddings(self, chunks, embeddings, index_name):
        """
        Armazena embeddings dos documentos no índice Pinecone.

        Args:
        - chunks (list): Lista de objetos Document representando os dados divididos.
        - embeddings (list): Lista de embeddings para os documentos.
        - index_name (str): Nome do índice onde os embeddings serão armazenados.

        Returns:
        - vector_store: O objeto de armazenamento vetorial criado.
        """
        logger.info(f"Armazenando embeddings no índice {index_name}...")

        # Armazena os embeddings no Pinecone usando a função from_documents
        vector_store = Pinecone.from_documents(chunks, embeddings, index_name=index_name)

        logger.success("Embeddings armazenados com sucesso no Pinecone.")
        return vector_store

