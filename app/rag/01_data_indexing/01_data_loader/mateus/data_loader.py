import base64
import logging
import base64
import requests

logging.basicConfig(level=logging.INFO)

class DataLoader:
    def load_data(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")


class Frontalmg(DataLoader):
    def __init__(self, image_path, openai_api_key):
        self.image_path = image_path
        self.openai_api_key = openai_api_key

    def load_data(self):
        
        with open(self.image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        try:
            PROMPT_MESSAGES = [

      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": 
                'É esperado quea imagem seja uma foto frontal, caso não seja por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM FRONTAL DE UM VEÍCULO.'
                
                'Caso a imagem seja uma foto frontal de um veículo extraia as informações da placa de um veículo, se possivel a marca e a cor do veículo'
                
                'Exemplo de placas'
                'Placa do veiculo: ABC-1234'
                'Placa do veiculo: CBA-1234'
                'Placa do veiculo: BCA-1234'
                'Placa do veiculo: ABC-1A34'

                'As cores devem vir sempre nesse formato'
                'Vermelho -> Vermelha'
                'Roxo -> Roxa'
                'Azul -> Azul'
                'Preto -> Preta'
                'Bege -> Bege'
                
                'Me retorne nesse formato especifico:'
                'Placa do veículo: Placa do veículo - Cor do veículo: Cor do veículo - Marca do veículo: Marca do veículo'
                  
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64, {base64_image}",
              "detail": "high"
            }
          }
        ]
      }
    ]
  
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }
            payload = {
                "model": "gpt-4o",  # Modelo que suporta visão computacional
                "messages": PROMPT_MESSAGES,
                "max_tokens": 2000
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            response_json = response.json()

            # Acessando o conteúdo da resposta
            content = response_json['choices'][0]['message']['content']
            content = content.strip().split('\n')
            # Retorna o conteúdo processado
            return content

        except Exception as e:
            logging.error(f"Erro ao processar os dados: {e}")
            return None

class Errorlmg(DataLoader):
    def __init__(self, image_path, openai_api_key):
        self.image_path = image_path
        self.openai_api_key = openai_api_key

    def load_data(self):
        
        with open(self.image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        try:
            PROMPT_MESSAGES = [

      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": 
                'É esperado que a imagem seja uma foto frontal, e a placa seja exclusivamente "ZYD-5L69"'
                'Caso a imagem seja um foto frontal e a placa não for igual a "POX4G21", por favor retorne ERROR: O ARQUVO CORRESPONDE A UMA IMAGEM FRONTAL DE UM VEÍCULO, PORÉM A PLACA NÃO CONFERE.'
                
                'Caso a imagem não seja uma foto frontal e a placa não for igual a "POX4G21", por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM FRONTAL E SIM {TIPO DA IMAGEM} DE UM VEÍCULO E A PLACA NÃO CONFERE.'
                
                'Caso a imagem não seja uma foto frontal e a placa for igual a "POX4G21", por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM FRONTAL E SIM {TIPO DA IMAGEM} DE UM VEÍCULO.'

                'Caso a imagem seja uma foto frontal, meio-frontal, lateral-frontal de um veículo e a placa for igual a "POX4G21" extraia as informações se possivel da marca e a cor do veículo'
                
                'Exemplo de placas'
                'Placa do veiculo: ABC-1234'
                'Placa do veiculo: CBA-1234'
                'Placa do veiculo: BCA-1234'
                'Placa do veiculo: ABC-1A34'

                'As cores devem vir sempre nesse formato'
                'Vermelho -> Vermelha'
                'Roxo -> Roxa'
                'Azul -> Azul'
                'Preto -> Preta'
                'Bege -> Bege'
                
                'Me retorne nesse formato especifico:'
                'Placa do veículo: Placa do veículo - Cor do veículo: Cor do veículo - Marca do veículo: Marca do veículo e a imagem em 30 200px se possivel'
                  
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64, {base64_image}",
              "detail": "high"
            }
          }
        ]
      }
    ]
  
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }
            payload = {
                "model": "gpt-4o",  # Modelo que suporta visão computacional
                "messages": PROMPT_MESSAGES,
                "max_tokens": 2000
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            response_json = response.json()

            # Acessando o conteúdo da resposta
            content = response_json['choices'][0]['message']['content']
            content = content.strip().split('\n')
            # Retorna o conteúdo processado
            return content

        except Exception as e:
            logging.error(f"Erro ao processar os dados: {e}")
            return None

class Traseiralmg(DataLoader):
    def __init__(self, image_path, openai_api_key):
        self.image_path = image_path
        self.openai_api_key = openai_api_key

    def load_data(self):
        
        with open(self.image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        try:
            PROMPT_MESSAGES = [

      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": 
                'É esperado quea imagem seja uma foto traseira, caso não seja por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM TRASEIRA DE UM VEÍCULO.'
                
                'Caso a imagem seja uma foto traseira de um veículo extraia as informações da placa de um veículo, se possivel a marca e a cor do veículo'
                
                'Exemplo de placas'
                'Placa do veiculo: ABC-1234'
                'Placa do veiculo: CBA-1234'
                'Placa do veiculo: BCA-1234'
                'Placa do veiculo: ABC-1A34'

                'As cores devem vir sempre nesse formato'
                'Vermelho -> Vermelha'
                'Roxo -> Roxa'
                'Azul -> Azul'
                'Preto -> Preta'
                'Bege -> Bege'
                
                'Me retorne nesse formato especifico:'
                'Placa do veículo: Placa do veículo - Cor do veículo: Cor do veículo - Marca do veículo: Marca do veículo'
                  
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64, {base64_image}",
              "detail": "high"
            }
          }
        ]
      }
    ]
  
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }
            payload = {
                "model": "gpt-4o",  # Modelo que suporta visão computacional
                "messages": PROMPT_MESSAGES,
                "max_tokens": 2000
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            response_json = response.json()

            # Acessando o conteúdo da resposta
            content = response_json['choices'][0]['message']['content']
            content = content.strip().split('\n')
            # Retorna o conteúdo processado
            return content

        except Exception as e:
            logging.error(f"Erro ao processar os dados: {e}")
            return None

class FileDataLoader(DataLoader):
    def __init__(self, image_path):
        self.image_path = image_path

    def load_data(self):
        # Carrega e codifica a imagem em base64
        try:
            with open(self.image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            return base64_image
        except Exception as e:
            logging.error(f"Erro ao carregar o arquivo: {e}")
            return None
        