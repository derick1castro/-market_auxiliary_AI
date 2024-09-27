import sys
import os
from data_indexer import DataIndexer
from loguru import logger

# Ajusta o sys.path para garantir que a pasta 'rag' seja encontrada
def add_to_sys_path(*directories):
    """
    Adiciona múltiplos diretórios ao sys.path.
    
    Args:
    - directories: Tupla de diretórios (relativos ou absolutos) a serem adicionados ao sys.path.
    """
    for directory in directories:
        abs_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), directory))
        if abs_directory not in sys.path:
            sys.path.append(abs_directory)

# Adiciona múltiplos diretórios ao sys.path
add_to_sys_path('..', '../../../')

# Importar os módulos normalmente
from config import config
from models import model

def main():
    """
    Função principal que realiza a indexação de dados usando embeddings do OpenAI
    e um indexador de dados personalizado. A função carrega a imagem e os embeddings
    e executa a indexação para o sistema configurado (como Pinecone).

    Etapas:
    - Carregar e inicializar os embeddings usando OpenAI.
    - Indexar os dados fornecidos usando um indexador (DataIndexer).
    - Exibir o resultado da indexação usando o `loguru`.

    Retorno:
    - Nenhum retorno explícito. Loga o resultado da operação de indexação.
    """
    
    logger.info("Iniciando o processo de indexação de dados.")

    # Cria uma instância do DataIndexer para realizar a indexação no Pinecone ou outro sistema
    data_indexer = DataIndexer()

    logger.info(f"Indexando a imagem localizada em: {config.IMAGE_PATH}")

    # Realiza a indexação dos dados (imagem e embeddings)
    index_result = data_indexer.index_data(index_name=config.INDEX_NAME, 
                                           data_source=config.IMAGE_PATH, 
                                           embeddings=model.EMBEDDING_MODEL)
    
    logger.success(f"Indexação concluída com sucesso!")

if __name__ == '__main__':
    """
    O ponto de entrada do programa. Chama a função `main()` para iniciar o processo de indexação.
    """
    main()
