import os
from dotenv import load_dotenv
from datetime import datetime

# Data e hora atual no formato ISO 8601
TODAY = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S-00:00')

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# API Key do OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Caminho da imagem que será processada
IMAGE_PATH = r'../../../data/raw/bh_1.png'

# Nome do índice de dados no banco de dados vetorial (ex: Pinecone)
INDEX_NAME = 'catalog-chat'

CHUNK_SIZE = 200

CHUNK_OVERLAP = CHUNK_SIZE*0.2

# Chave da API do Pinecone
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# Configurações do Pinecone
INDEX_NAME = 'catalog-chat'
DIMENSION = 1536
METRIC = 'cosine'
CLOUD_PROVIDER = 'aws'
REGION = 'us-east-1'
