import base64
import requests
import os
from dotenv import load_dotenv
import openai
import pandas as pd


# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Path to your image
image_path1 = r'../../data/raw/bh/1.png'
image_path2 = r'../../data/raw/bh/2.png'
image_path4 = r'../../data/raw/bh/4.png'

filename = image_path1.split('/')[-1]

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Obtendo as imagens codificadas em base64
base64_image1 = encode_image(image_path1)
base64_image2 = encode_image(image_path2)
base64_image4 = encode_image(image_path4)

images = [base64_image1, base64_image2, base64_image4]
partes = []


PROMPT_MESSAGES_BH = [

    {
    "role": "user",
    "content": [
        {
        "type": "text",
        "text": 
                'Extraia todas as seguintes informações dos encartes.'
                
                'Por favor não retorne a estrutura nesse formato'
                '{Número}. {Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - Supermercados BH'
                
                'Por favor me retorne essa estrutura, siga rigorosamente o seguinte padrão para cada produto:'
                '{Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - Supermercados BH'
                
                'Exemplo:'
                'Macarrão Adria Cortes 500g - R$ 2,09 - Mercearia - Supermercados BH'
                'Azeite Extra Virgem Rahma 500ml - R$ 12,90 - Mercearia - Supermercados BH'
                'Café Pilão Tipo 500g - R$ 8,39 - Grãos - Supermercados BH'

                'Por favor, utilize as seguintes categorias para os produtos:'
                '- Frango'
                '- Laticínio'
                '- Mercearia'
                '- Bebidas'
                '- Frios'
                '- Peixes e Frutos do Mar'
                'Caso não haja outras categorias, pode ignora-las'

                'Esse glossário cobre várias categorias comuns encontradas em encartes de supermercado, facilitando a classificação dos produtos.'
                'Glossário de categorias:'
                '- Fielzinho de Frango – Frango'
                '- Iogurte – Laticínio'
                '- Leite – Laticínio'
                '- Arroz Branco – Mercearia'
                '- Feijão Carioca – Mercearia'
                '- Atum – Peixes e Frutos do Mar'
                '- Cerveja Pilsen – Bebidas'
                '- Refrigerante de Cola – Bebidas'
                '- Biscoito Recheado – Mercearia'
                '- Queijo Mussarela – Laticínio'
                '- Presunto Cozido – Frios'
                '- Manteiga com Sal – Laticínio'
                '- Macarrão Espaguete – Mercearia'
                '- Azeite de Oliva – Mercearia'
                '- Água Mineral – Bebidas'
                '- Filé de Peixe Congelado – Peixes e Frutos do Mar'

                'Certifique-se de que todas as informações estejam no formato correto para fácil indexação e armazenamento em um sistema de vector store.'
                
                'Preste a atenção no separador, dever ser "-" e não "–".'
                'Por favor, siga rigorosamente o seguinte padrão para cada produto e não saia do padrão fornecido'
                
                'Glossário do nome do estabelecimento:'
                'bh, BH, Bh ou bH - Supermercados BH'
        },
        {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{img}",
            "detail": "high"
        }
        }
    ]
    }
]
headers_BH = {
"Content-Type": "application/json",
"Authorization": f"Bearer {openai_api_key}"
}
payload_BH = {
"model": "chatgpt-4o-latest",
"messages": PROMPT_MESSAGES_BH,
"max_tokens": 2000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers_BH, json=payload_BH)

# Verificando a resposta
response_json = response.json()

# Acessando o conteúdo da resposta (content)
content = response_json['choices'][0]['message']['content'].strip().split('\n')
partes += content



PROMPT_MESSAGES = [

    {
    "role": "user",
    "content": [
        {
        "type": "text",
        "text": 
                'Extraia todas as seguintes informações dos encartes.'
                
                'Por favor não retorne a estrutura nesse formato'
                '{Número}. {Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - {Nome do Estabelecimento}'
                
                'Por favor me retorne essa estrutura, siga rigorosamente o seguinte padrão para cada produto:'
                '{Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - {Nome do Estabelecimento}'
                
                'Exemplo:'
                'Macarrão Adria Cortes 500g - R$ 2,09 - Mercearia - Assaí Atacadista'
                'Azeite Extra Virgem Rahma 500ml - R$ 12,90 - Mercearia - Assaí Atacadista'
                'Café Pilão Tipo 500g - R$ 8,39 - Grãos - BH'

                'Por favor, utilize as seguintes categorias para os produtos:'
                '- Frango'
                '- Laticínio'
                '- Mercearia'
                '- Bebidas'
                '- Frios'
                '- Peixes e Frutos do Mar'
                'Caso não haja outras categorias, pode ignora-las'

                'Esse glossário cobre várias categorias comuns encontradas em encartes de supermercado, facilitando a classificação dos produtos.'
                'Glossário de categorias:'
                '- Fielzinho de Frango – Frango'
                '- Iogurte – Laticínio'
                '- Leite – Laticínio'
                '- Arroz Branco – Mercearia'
                '- Feijão Carioca – Mercearia'
                '- Atum – Peixes e Frutos do Mar'
                '- Cerveja Pilsen – Bebidas'
                '- Refrigerante de Cola – Bebidas'
                '- Biscoito Recheado – Mercearia'
                '- Queijo Mussarela – Laticínio'
                '- Presunto Cozido – Frios'
                '- Manteiga com Sal – Laticínio'
                '- Macarrão Espaguete – Mercearia'
                '- Azeite de Oliva – Mercearia'
                '- Água Mineral – Bebidas'
                '- Filé de Peixe Congelado – Peixes e Frutos do Mar'

                'Certifique-se de que todas as informações estejam no formato correto para fácil indexação e armazenamento em um sistema de vector store.'
                
                'Preste a atenção no separador, dever ser "-" e não "–".'
                'Por favor, siga rigorosamente o seguinte padrão para cada produto e não saia do padrão fornecido'
        },
        {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{img}",
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
"model": "chatgpt-4o-latest",
"messages": PROMPT_MESSAGES,
"max_tokens": 7000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Verificando a resposta
response_json = response.json()

# Acessando o conteúdo da resposta (content)
content = response_json['choices'][0]['message']['content'].strip().split('\n')
partes += content

df = pd.DataFrame(partes)
df[['Produto','Valor', 'Categoria', 'Local']] = df[0].str.split(r'\d+\.\s|- ', expand=True)
df = df.drop(columns=[ 0], axis=1).dropna().reset_index(drop=True)
df