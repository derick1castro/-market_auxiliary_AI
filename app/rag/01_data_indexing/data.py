# data.py

import requests
import logging
from dotenv import load_dotenv
import os
import base64
load_dotenv()

class DataEmbedder:
    def __init__(self):
        pass
    def embed_data(self):
        image_path=r'C:\Users\Derick\Desktop\Projetos_ia\project-root\data\raw\bh_1.png'
        openai_api_key = os.getenv('OPENAI_API_KEY')
        
        with open(image_path, "rb") as image_file:
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
                "Authorization": f"Bearer {openai_api_key}"
            }
            payload = {
                "model": "chatgpt-4o-latest",  # Modelo que suporta visão computacional
                "messages": PROMPT_MESSAGES,
                "max_tokens": 7000
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            response_json = response.json()

            # Acessando o conteúdo da resposta
            # content = response_json['choices'][0]['message']['content'].strip()
            # Retorna o conteúdo processado
            return response_json

        except Exception as e:
            logging.error(f"Erro ao processar os dados: {e}")
            return None
