# Análise de Encartes de Promoções com RAG (Retrieval Augmented Generation) e OpenAI GPT-Vision

## Descrição
Este projeto utiliza inteligência artificial para analisar encartes de promoções de supermercados e responder a perguntas complexas, como onde determinados itens estão mais baratos e realizar comparações entre produtos e locais. Utilizando a nova API GPT-Vision da OpenAI, o sistema é capaz de processar imagens dos encartes, extrair informações sobre produtos e preços, e fornecer respostas relevantes para perguntas dos usuários.

O pipeline do projeto está dividido em duas fases principais: **Indexação de Dados** e **Data Retrieval & Generation** (Consulta e Geração de Respostas), com integração a bancos de dados vetoriais como o Pinecone para garantir respostas precisas e eficientes.

## Tecnologias
- **OpenAI GPT-Vision API**: Visão computacional e entendimento de imagens.
- **Langchain**: Criação de pipelines RAG (Retrieval Augmented Generation).
- **Pinecone**: Banco de dados vetorial para armazenamento e recuperação de embeddings.
- **Python**: Desenvolvimento de toda a lógica do pipeline.
- **Orientação a Objetos (OOP)**: Estrutura modular e escalável do código.

## Atividades Realizadas

### Pipeline de Indexação de Dados:

1. **Carregamento de Dados (Data Loading)**:
   - Processamento de encartes de promoção em formato de imagem, utilizando GPT-Vision para reconhecer e extrair os dados textuais.
   
2. **Divisão de Dados (Data Splitting)**:
   - Segmentação dos dados textuais extraídos em chunks menores, prontos para serem embeddados e indexados.
   
3. **Geração de Embeddings (Data Embedding)**:
   - Utilização de embeddings vetoriais, como `text-embedding-ada-002`, para transformar os chunks de texto em representações vetoriais.
   
4. **Armazenamento em Banco de Dados Vetorial (Data Storing)**:
   - Integração com o Pinecone para indexar os embeddings, facilitando a recuperação eficiente durante as consultas.

5. **Arquitetura Baseada em OOP (Orientação a Objetos)**:
   - Estruturação do projeto com uma abordagem orientada a objetos, garantindo modularidade, escalabilidade e facilidade de manutenção.

## Próximas Atividades

### Data Retrieval & Generation:

1. **Consulta de Dados (User Query)**:
   - Implementação de uma interface de perguntas onde os usuários podem fazer consultas, como "Onde posso encontrar o produto X mais barato?".

2. **Geração de Embeddings para a Consulta**:
   - A consulta do usuário será transformada em embeddings vetoriais para que possa ser comparada aos dados indexados.

3. **Recuperação dos Dados no Banco Vetorial (Vector DB Retrieval)**:
   - Utilização do Pinecone para encontrar os **Top-k chunks** mais relevantes que correspondam à consulta do usuário.

4. **Geração de Respostas (LLM - Large Language Model)**:
   - Utilização do modelo GPT para processar os dados recuperados e gerar uma resposta contextual e precisa para o usuário.

5. **Melhoria do Fluxo de Geração de Respostas**:
   - Aprimorar o fluxo de geração para que seja ágil e compreensível, gerando respostas em linguagem natural baseadas nas informações extraídas dos encartes.
