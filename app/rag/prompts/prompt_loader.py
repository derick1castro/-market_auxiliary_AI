# prompts.py

PROMPT_TEMPLATE = """
    Extraia todas as seguintes informações dos encartes.

    Por favor, não retorne a estrutura nesse formato: 
    {Número}. {Nome do Produto} - {Valor do Produto} - {Categoria do Produto} - {Nome do Estabelecimento}

    Siga rigorosamente o seguinte padrão para cada produto:
    {Nome do produto}: Nome - {Valor do produto}: Valor - {Categoria do produto}: Categoria - {Nome do estabelecimento}: Estabelecimento

    Exemplo:
    Nome do produto: Macarrão Adria Cortes 500g - Valor do produto: R$ 2,09 - Categoria do produto: Mercearia - Nome do estabelecimento: Assaí Atacadista
    Nome do produto: Azeite Extra Virgem Rahma 500ml - Valor do produto: R$ 12,90 - Categoria do produto: Mercearia - Nome do estabelecimento: Assaí Atacadista
    Nome do produto: Café Pilão Tipo 500g - Valor do produto: R$ 8,39 - Categoria do produto: Grãos - Nome do estabelecimento: BH

    Por favor, utilize as seguintes categorias para os produtos:
    A categoria do produto só deve ser retornada com os itens abaixo:
    - Frango
    - Laticínio
    - Mercearia
    - Bebidas
    - Frios
    - Peixes e Frutos do Mar

    Caso não haja outras categorias, pode ignorá-las.

    Esse glossário cobre várias categorias comuns encontradas em encartes de supermercado:
    - Fielzinho de Frango – Frango
    - Iogurte – Laticínio
    - Leite – Laticínio
    - Arroz Branco – Mercearia
    - Feijão Carioca – Mercearia
    - Atum – Peixes e Frutos do Mar
    - Cerveja Pilsen – Bebidas
    - Refrigerante de Cola – Bebidas
    - Biscoito Recheado – Mercearia
    - Queijo Mussarela – Laticínio
    - Presunto Cozido – Frios
    - Manteiga com Sal – Laticínio
    - Macarrão Espaguete – Mercearia
    - Azeite de Oliva – Mercearia
    - Água Mineral – Bebidas
    - Filé de Peixe Congelado – Peixes e Frutos do Mar

    Preste atenção ao separador: deve ser "-" e não "–".
    Por favor, siga rigorosamente o seguinte padrão para cada produto e não saia do padrão fornecido.
    """

def generate_image_prompt(base64_image):
    """
    Gera o prompt final que inclui a imagem em base64 e o template de prompt.

    Args:
    - base64_image (str): A imagem codificada em base64.

    Returns:
    - dict: O prompt completo, pronto para ser enviado à API do OpenAI.
    """
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": PROMPT_TEMPLATE
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
