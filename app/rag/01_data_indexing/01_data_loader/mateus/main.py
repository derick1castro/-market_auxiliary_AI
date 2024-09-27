
from data_loader import Frontalmg
from data_loader import Traseiralmg
from data_loader import Errorlmg
import os
from dotenv import load_dotenv
import logging
from tkinter import*
import time
logging.basicConfig(level=logging.INFO)

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
traseira = r'../../../../../data/raw/veiculo.jpg'
frontal = r'../../../../../data/raw/veiculo2.jpg'
nao_apl = r'../../../../../data/raw/veiculo3.jpg'



def main():
    
    '''
        É esperado quea imagem seja uma foto frontal, 
        caso não seja por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM FRONTAL DE UM VEÍCULO.
        
    '''
    def frontal_img(img):
        janela = Tk()
        janela.title('Analisador de imagens para o MEV')
        janela.geometry('900x40')
        
        img_processor = Frontalmg(img, openai_api_key)
        img_frontal = img_processor.load_data()
        img_frontal
        
        label = Label(janela,
                    text= img_frontal, 
                    font=('Arial Bold', 15))
        label.pack()
        janela.after(10000, janela.destroy)
        janela.mainloop()
        
    frontal_img(frontal)
    
    
    
    '''
        É esperado que a imagem seja uma foto frontal, e a placa seja exclusivamente "ZYD-5L69"
        
        Caso a imagem seja um foto frontal e a placa não for igual a "POX4G21", por favor retorne ERROR: O ARQUVO CORRESPONDE A UMA IMAGEM FRONTAL DE UM VEÍCULO, PORÉM A PLACA NÃO CONFERE.
        
                
        Caso a imagem não seja uma foto frontal e a placa não for igual a "POX4G21", por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM FRONTAL E SIM {TIPO DA IMAGEM} DE UM VEÍCULO E A PLACA NÃO CONFERE.
        
                
        Caso a imagem não seja uma foto frontal e a placa for igual a "POX4G21", por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM FRONTAL E SIM {TIPO DA IMAGEM} DE UM VEÍCULO.
    '''
    def traseira_img(img):
        
        janela = Tk()
        janela.title('Analisador de imagens para o MEV')
        janela.geometry('900x40')
        
        img_processor = Traseiralmg(img, openai_api_key)
        img_traseira = img_processor.load_data()
        img_traseira
        
        label = Label(janela,
                    text= img_traseira, 
                    font=('Arial Bold', 15))
        label.pack()
        janela.after(10000, janela.destroy)

        janela.mainloop()
    
    #traseira_img(frontal)
    traseira_img(traseira)
    
    '''
        É esperado quea imagem seja uma foto traseira, caso não seja por favor retorne ERROR: O ARQUVO NÃO CORRESPONDE A UMA IMAGEM TRASEIRA DE UM VEÍCULO.
                
        Caso a imagem seja uma foto traseira de um veículo extraia as informações da placa de um veículo, se possivel a marca e a cor do veículo.
    '''
    def error_img(img):
        janela = Tk()
        janela.title('Analisador de imagens para o MEV')
        janela.geometry('900x40')
        
        img_processor = Errorlmg(img, openai_api_key)
        img_nao_apl = img_processor.load_data()
        img_nao_apl
        
        label = Label(janela,
                    text= img_nao_apl, 
                    font=('Arial Bold', 15))
        label.pack()
        janela.after(10000, janela.destroy)
        janela.mainloop()
        
    error_img(frontal)
    error_img(traseira)
    error_img(nao_apl)

    

if __name__ == "__main__":
    main()
