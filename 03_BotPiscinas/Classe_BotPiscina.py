# doutorpiscinas2@gmail.com
from google import genai
from google.genai import types
import ttkbootstrap as ttk


class BotPiscinas:
    def __init__(self):
        self.janela = ttk.Window(themename="solar")
        self.janela.title("Doutor Piscinas")
        self.janela.iconbitmap("03_BotPiscinas/icon/piscina.ico")
        self.janela.geometry("1280x720+260+160") #Aumentando a tela
        self.janela.resizable(False, False) # Para nao deixar o usuario aumentar ou diminuir a tela

        # texto doutor piscinas
        self.textoprincipal = ttk.Label(self.janela, 
                                        text="Doutor Piscinas",
                                        padding=10,
                                        font=("Segoe UI", 24) 
                                        )
        self.textoprincipal.pack()

        # Descricao do doutor piscinas
        self.descricao = ttk.Label(self.janela, 
                                   text="O doutor piscinas é um especialista com \n mais de 1005 Anos de carreira, pergunte qualquer \ncoisa sobre piscinas, ele irá saber!",
                                   font=("Arial",12),
                                   padding=10
        )
        self.descricao.pack()

        # Campo para pergunta para i.a
        self.campo_pergunta = ttk.Entry(self.janela)
        self.campo_pergunta.pack()

        # Botao de enviar pergunta

        self.botao_envio = ttk.Button(text="Perguntar ao Doutor", 
                                      command=self.enviar_pergunta
                                      )
        self.botao_envio.pack()

        # Label resposta da i.a
        
        self.label_retorno = ttk.Label(text="",
                                       font=("Times New Roman", 11),
                                       padding=10,
                                       width=30
                                    
                                       )
        self.label_retorno.pack()
        
    def run(self):
        """Funcao para deixar a janela em looping"""
        self.janela.mainloop()


    def enviar_pergunta(self):
        """Funcao para o botao de enviar pergunta"""

        self.pergunta = self.campo_pergunta.get()

        #Parte da i.a
        client = genai.Client(api_key="AIzaSyAqHTr0DulKHBhwpSIeIEZv4QSo0lfiHX8")

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction="Você é um especialista em piscinas, com mais de 1005 anos no mercado, você entende tudo, é o melhor de todos, o mais reconhecido em toda a historia"),
            contents=f"{self.pergunta}"
        )

        
        self.label_retorno.config(text=f"Resposta do DoutorPiscinas: \n {response.text}")

        

