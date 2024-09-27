import sys
import os
import base64
import requests
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
from prompts.prompt_loader import generate_image_prompt

class DataLoader:
    """
    Classe base abstrata para carregamento de dados. Subclasses devem implementar o método load_data.
    """
    def load_data(self):
        """
        Método abstrato para carregar dados.

        Raises:
        - NotImplementedError: Se o método não for implementado por uma subclasse.
        """
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")


class ImgDataLoader(DataLoader):
    """
    Classe para carregar e processar dados de imagens, usando a API do OpenAI para extrair informações.
    """
    def __init__(self, image_path, openai_api_key=config.OPENAI_API_KEY):
        """
        Inicializa o ImgDataLoader com o caminho da imagem e a chave da API do OpenAI.

        Args:
        - image_path (str): O caminho para a imagem a ser processada.
        - openai_api_key (str): A chave da API do OpenAI.
        """
        self.image_path = image_path
        self.openai_api_key = openai_api_key

    def load_data(self):
        """
        Carrega a imagem, codifica em base64 e envia para a API do OpenAI para extrair informações.

        Returns:
        - list: Uma lista de strings contendo as informações processadas.
        """
        try:
            # Codifica a imagem em base64
            with open(self.image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')

            # Define a mensagem e a payload para o modelo do OpenAI
            # Gera o prompt utilizando o método centralizado
            prompt_messages = generate_image_prompt(base64_image)
  
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }
            payload = {
                "model": model.GPT_MODEL,  # Modelo que suporta visão computacional
                "messages": prompt_messages,
                "max_tokens": model.MAX_TOKENS
            }

            # Faz a requisição à API do OpenAI
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            response.raise_for_status()  # Garante que exceções HTTP sejam tratadas

            response_json = response.json()

            # Acessa o conteúdo da resposta e processa
            content = response_json['choices'][0]['message']['content']
            content = content.strip().split('\n')
            
            # Retorna o conteúdo processado
            logger.info("Dados carregados e processados com sucesso.")
            return content

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição à API do OpenAI: {e}")
            return None
        except Exception as e:
            logger.error(f"Erro ao processar os dados: {e}")
            return None

# class FileDataLoader(DataLoader):
#     def __init__(self, image_path):
#         self.image_path = image_path

#     def load_data(self):
#         # Carrega e codifica a imagem em base64
#         try:
#             with open(self.image_path, "rb") as image_file:
#                 base64_image = base64.b64encode(image_file.read()).decode('utf-8')
#             return base64_image
#         except Exception as e:
#             logging.error(f"Erro ao carregar o arquivo: {e}")
#             return None
        