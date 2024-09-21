import base64
import requests
import os
from dotenv import load_dotenv


# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# OpenAI API Key
api_key = os.getenv('OPENAI_API_KEY')


# Path to your image
image_path = r"C:\Users\Derick\Desktop\Projetos_ia\project-root\app\processor\395afd9106cf9a227e19c3f19ed94baf.jpg"
image_path2 = r"C:\Users\Derick\Desktop\Projetos_ia\project-root\app\processor\123.jpg"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text":
                "Extraia todas as seguintes informações do encarte:"

                'Cada item deve incluir o nome completo, valor e peso/quantidade.'
                '1. Nome do produto'
                '2. Valor do produto'
                '3. Peso ou quantidade do produto'
                '4. Categoria do produto'

                
                'E obrigatoriamente seguir esse padrão por exemplo:'
                'Supermercado: Assaí Atacadista'
                '{Produto 1: Macarrão Adria Cortes 500g - Valor: R$ 2,09 - Mercearia}'
                '{Produto 2: Azeite Extra Virgem Rahma 500ml - Valor: R$ 12,90 - Mercearia}'
                '{Produto 3: Café Pilão Tipo 500g - Valor: R$ 839 - Grãos}'
                
                'Esse glossário cobre várias categorias comuns encontradas em encartes de supermercado, facilitando a classificação dos produtos.'
                'Fielzinho de Frango – Frango'
                'Iogurte – Laticínio'
                'Leite – Laticínio'
                'Arroz Branco – Mercearia'
                'Feijão Carioca – Mercearia'
                'Cerveja Pilsen – Bebidas'
                'Refrigerante de Cola – Bebidas'
                'Biscoito Recheado – Mercearia'
                'Queijo Mussarela – Laticínio'
                'Presunto Cozido – Frios'
                'Manteiga com Sal – Laticínio'
                'Macarrão Espaguete – Mercearia'
                'Azeite de Oliva – Mercearia'
                'Água Mineral – Bebidas'
                'Filé de Peixe Congelado – Peixes e Frutos do Mar'
                
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
  ],
  "max_tokens": 900
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Verificando a resposta
response_json = response.json()

# Acessando o conteúdo da resposta (content)
content = response_json['choices'][0]['message']['content']

content.split('\n')