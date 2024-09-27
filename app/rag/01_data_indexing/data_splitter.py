import re
import os
import sys
from langchain_text_splitters import RecursiveCharacterTextSplitter
from loguru import logger

# Ajusta o sys.path para garantir que a pasta 'rag' seja encontrada
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o arquivo config do projeto
from config import config

class DataSplitter:
    
    """
    Classe base abstrata para dividir dados. As subclasses devem implementar o método split_data.
    """
    
    def split_data(self):
        
        """
        Método abstrato para ser implementado pelas subclasses.
        """
        
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class SimpleDataSplitter(DataSplitter):
    
    """
    Divisor de dados que utiliza o RecursiveCharacterTextSplitter para dividir dados textuais
    em chunks menores e adiciona metadados ao conteúdo dividido.
    """
    
    def __init__(self, chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP):
        
        """
        Inicializa o divisor de dados com um tamanho de chunk e um tamanho de sobreposição.
        
        Args:
        - chunk_size (int): O tamanho máximo de cada chunk.
        - chunk_overlap (int): Quantidade de sobreposição entre os chunks.
        """
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""],
            length_function=len,
            is_separator_regex=False
        )

    def split_data(self, data):
        
        """
        Divide os dados textuais em chunks menores e adiciona metadados extraídos do texto.

        Args:
        - data (list): Lista de strings representando os dados a serem divididos.

        Returns:
        - list: Uma lista de objetos Document com o conteúdo dividido e metadados associados.
        """
        
        splitted = []
        for lista_dados in data:
            logger.info("Processando dados...")

            # Extrai o nome do estabelecimento para adicionar ao metadado.
            estabelecimento = re.search(r"Nome do estabelecimento:\s*([^,]*)", lista_dados)
            if estabelecimento:
                estabelecimento = estabelecimento.group(1)
            else:
                estabelecimento = ''
            
            # Extrai a categoria do produto para adicionar ao metadado.
            categoria_produto = re.search(r'Categoria do produto:\s*([^\s-]+)', lista_dados)
            if categoria_produto:
                categoria_produto = categoria_produto.group(1)
            else:
                categoria_produto = ''
            
            logger.info(f"Estabelecimento: {estabelecimento}, Categoria: {categoria_produto}")

            # Verifica se o dado é uma string e divide o conteúdo em chunks menores.
            if isinstance(lista_dados, str): 
                documents = self.text_splitter.create_documents([lista_dados])
            elif isinstance(data, list):   
                documents = self.text_splitter.create_documents(data)
            
            # Adiciona os metadados a cada documento gerado.
            for doc in documents:
                doc.metadata.update({
                    'Nome do estabelecimento': estabelecimento,
                    'Categoria do produto': categoria_produto,
                    'updated_at': config.TODAY  # Data de atualização
                })
                splitted.append(doc)
        
        logger.success(f"{len(splitted)} documentos processados e divididos.")
        return splitted

