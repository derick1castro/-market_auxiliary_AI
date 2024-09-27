import sys
import os
from data_splitter import SimpleDataSplitter
from data_store import PineconeDataStore
from data_loader import ImgDataLoader
from loguru import logger

# Ajusta o sys.path para garantir que a pasta 'rag' seja encontrada
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o arquivo config do projeto
from config import config

class DataIndexer:
    """
    Classe responsável por processar, dividir e indexar dados em um armazenamento vetorial,
    como Pinecone, utilizando embeddings do OpenAI.

    Métodos:
    - index_data(index_name, data_source, embeddings): Realiza o processo de indexação dos dados.
    """

    def __init__(self):
        """
        Inicializa a classe DataIndexer sem argumentos adicionais.
        Pode ser estendido futuramente para aceitar mais parâmetros de configuração.
        """
        pass

    def index_data(self, index_name, data_source, embeddings):
        """
        Executa o processo de indexação de dados.

        Etapas:
        1. Carrega e processa os dados da imagem ou outro tipo de fonte.
        2. Divide os dados em chunks.
        3. Armazena os dados no banco de dados vetorial (como Pinecone).

        Args:
        - index_name (str): O nome do índice de dados a ser usado no banco de dados vetorial.
        - data_source (str): O caminho para a imagem ou outro tipo de arquivo de dados.
        - embeddings (object): O modelo de embeddings para transformar os dados em vetores.

        Retorna:
        - vector_store: O armazenamento vetorial final após a indexação.
        """
        
        # Carrega e processa a imagem usando ImgDataLoader
        logger.info(f"Processando dados a partir de: {data_source}")
        img_processor = ImgDataLoader(data_source, config.OPENAI_API_KEY)
        data_loader = img_processor.load_data()
        logger.info("Dados processados com sucesso.")

        # Divide os dados carregados em chunks usando SimpleDataSplitter
        split = SimpleDataSplitter()
        data_splited = split.split_data(data_loader)
        logger.info("Dados separados em chunks.")

        # Armazena os dados processados e divididos no Pinecone
        logger.info(f"Conectando ao banco de dados vetorial: {index_name}")
        conecting_vector_store = PineconeDataStore(index_name)
        vector_store = conecting_vector_store.store_embeddings(data_splited, embeddings, index_name=index_name)
        logger.success("Dados indexados com sucesso!")

        return vector_store
