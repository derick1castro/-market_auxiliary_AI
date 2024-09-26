from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

# data = '''Produto muito longo com várias informações sobre o item que podem incluir especificações, comentários adicionais, instruções de uso, e outras características. Produto: Bebida Energética, Quantidade: 500ml, Preço: R$ 7,00. Disponível em várias regiões. \nOutro produto com uma descrição igualmente longa que deve ser fragmentada apropriadamente para evitar que a informação seja perdida ou cortada de maneira inadequada. Produto: Refrigerante, Quantidade: 1,5L, Preço: R$ 5,50. Descrição detalhada e mais informações sobre o produto.'''
class DataSplitter:
    def split_data(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class SimpleDataSplitter(DataSplitter):
    def __init__(self, chunk_size=200, chunk_overlap=40):
        # Configura o text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                                            chunk_overlap=chunk_overlap,
                                                            separators=["\n\n", "\n", " ", ""],
                                                            length_function =len,
                                                            is_separator_regex=False
                                                            )
    
    def _convert_to_documents(self, data):
        """
        
            Converte string ou lista de strings para uma lista de objetos Document.
            
        """
        if isinstance(data, str):
            return [Document(page_content=data, metadata={})]
        elif isinstance(data, list):
            return [Document(page_content=doc, metadata={}) for doc in data]
        else:
            raise ValueError("docs precisa ser uma string ou uma lista de strings")
    
    def split_data(self, data):
        # Converter 'docs' para uma lista de `Document` se for uma string ou lista de strings
        documents = self._convert_to_documents(data)  
              
        # Divide os documentos em partes menores
        return self.text_splitter.split_documents(documents)
        

    
    
