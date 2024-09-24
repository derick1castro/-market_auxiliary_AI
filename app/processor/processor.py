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
image_path1 = r"C:\Users\Derick\Desktop\Projetos_ia\project-root\app\processor\395afd9106cf9a227e19c3f19ed94baf.jpg"
image_path2 = r"C:\Users\Derick\Desktop\Projetos_ia\project-root\app\processor\123.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Obtendo as imagens codificadas em base64
base64_image1 = encode_image(image_path1)
base64_image2 = encode_image(image_path2)

# Getting the base64 string
base64_image = encode_image(image_path1)
base64_image2 = encode_image(image_path2)

PROMPT_MESSAGES = [

    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": 
                'Você é um assistente especializado e atento em analisar encartes de supermercado.'
                'Extraia todas as seguintes informações dos encartes e exclusivamente aos produtos mesmo que acha informações repetidas ou parecidas:'
                
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
            "url": f"data:image/jpeg;base64,{base64_image}",
            "detail": "high"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image2}",
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
  "max_tokens": 1500
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Verificando a resposta
response_json = response.json()

# Acessando o conteúdo da resposta (content)
content = response_json['choices'][0]['message']['content'].strip().split('\n')
content

df = pd.DataFrame(content)
df[['Index','Produto','Valor', 'Categoria', 'Local']] = df[0].str.split(r'\d+\.\s|- ', expand=True)
df = df.drop(columns=['Index', 0], axis=1).dropna().reset_index(drop=True)
df