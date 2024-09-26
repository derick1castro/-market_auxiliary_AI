
from data_indexer import DataIndexer
from data_loader import FileDataLoader
from data_splitter import SimpleDataSplitter
from data_embedder import OpenAIDataEmbedder
import os
from dotenv import load_dotenv
import openai
import pandas as pd
# from data_store import PineconeDataStore
import logging

logging.basicConfig(level=logging.INFO)
from data_loader import ImgDataLoader
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
image_path = r'../../../data/raw/bh_1.png'


# Outros imports necessários, como logging

def main():
###### IMG PROCESSOR ######
    # Configurações e parâmetros
    img_processor = ImgDataLoader(image_path, openai_api_key)
    # Inicializa os componentes
    data_loader = img_processor.load_data()
######################

###### SPLITTER ######
    splitter = SimpleDataSplitter()
    data_splited = splitter.split_data(data_loader)
######################
    embd = OpenAIDataEmbedder()
    embedded = embd.embedding_data(data_splited)
    # Exibe o resultado
    print("Resultado obtido:")
    print(data_loader)

if __name__ == "__main__":
    main()
