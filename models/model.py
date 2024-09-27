import sys
import os
from langchain.embeddings import OpenAIEmbeddings

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
add_to_sys_path('..', '../models')

# Agora você pode importar os módulos normalmente
from config import config

EMBEDDING_MODEL = OpenAIEmbeddings(api_key=config.OPENAI_API_KEY, model="text-embedding-ada-002")
GPT_MODEL = 'chatgpt-4o-latest'
MAX_TOKENS = 3000