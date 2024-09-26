import base64
import logging
import base64
import requests

logging.basicConfig(level=logging.INFO)

class DataLoader:
    def load_data(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")


class ImgDataLoader(DataLoader):
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
                            "text": (
                                'Extraia todas as seguintes informações dos encartes.\n'
                                'Por favor não retorne a estrutura nesse formato: '
                                '{Número}. {Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - {Nome do Estabelecimento}\n'
                                'Por favor me retorne essa estrutura, siga rigorosamente o seguinte padrão para cada produto:\n'
                                '{Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - {Nome do Estabelecimento}\n'
                                'Exemplo:\n'
                                'Macarrão Adria Cortes 500g - R$ 2,09 - Mercearia - Assaí Atacadista\n'
                                'Azeite Extra Virgem Rahma 500ml - R$ 12,90 - Mercearia - Assaí Atacadista\n'
                                'Café Pilão Tipo 500g - R$ 8,39 - Grãos - BH\n'
                                'Por favor, utilize as seguintes categorias para os produtos:\n'
                                '- Frango\n'
                                '- Laticínio\n'
                                '- Mercearia\n'
                                '- Bebidas\n'
                                '- Frios\n'
                                '- Peixes e Frutos do Mar\n'
                                'Caso não haja outras categorias, pode ignorá-las.\n'
                                'Esse glossário cobre várias categorias comuns encontradas em encartes de supermercado, facilitando a classificação dos produtos.\n'
                                'Glossário de categorias:\n'
                                '- Fielzinho de Frango – Frango\n'
                                '- Iogurte – Laticínio\n'
                                '- Leite – Laticínio\n'
                                '- Arroz Branco – Mercearia\n'
                                '- Feijão Carioca – Mercearia\n'
                                '- Atum – Peixes e Frutos do Mar\n'
                                '- Cerveja Pilsen – Bebidas\n'
                                '- Refrigerante de Cola – Bebidas\n'
                                '- Biscoito Recheado – Mercearia\n'
                                '- Queijo Mussarela – Laticínio\n'
                                '- Presunto Cozido – Frios\n'
                                '- Manteiga com Sal – Laticínio\n'
                                '- Macarrão Espaguete – Mercearia\n'
                                '- Azeite de Oliva – Mercearia\n'
                                '- Água Mineral – Bebidas\n'
                                '- Filé de Peixe Congelado – Peixes e Frutos do Mar\n'
                                'Certifique-se de que todas as informações estejam no formato correto para fácil indexação e armazenamento em um sistema de vector store.\n'
                                'Preste atenção no separador, deve ser "-" e não "–".\n'
                                'Por favor, siga rigorosamente o padrão fornecido e não saia dele.'
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
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
                "model": "gpt-4o-mini",  # Modelo que suporta visão computacional
                "messages": PROMPT_MESSAGES,
                "max_tokens": 1000
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
        