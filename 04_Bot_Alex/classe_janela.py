from classe_robo import Gemini_Bot
import ttkbootstrap as ttk

class Janela_Bot:
    def __init__(self):
        #Iniciando robo
        self.chat = Gemini_Bot()

        # Criando a janela em si
        self.janela = ttk.Window(themename="superhero")
        self.janela.title("Zeca Piscineiro")

        #Definindo icone, tamanho e impossibilitando para mexer na altura e largura
        self.janela.iconbitmap("04_Bot_Alex/icons/professor.ico")
        self.janela.geometry("1280x720+260+160")
        self.janela.resizable(False, False)

        #Criando textos principais 
        self.titulo1 = ttk.Label(text="Zeca Piscineiro",
                                 font=("Segoe UI", 20)
                                 )
        self.titulo1.pack(padx=10, pady=10)

        # Campo de pergunta

        self.campo_pergunta = ttk.Entry(width=50)
        self.campo_pergunta.pack(padx=10, pady=10)

        # RESPOSTA DA I.A
        self.label_retorno = ttk.Text(width=80,
                                       wrap="word",
                                       state="disabled",
                                       pady=20
                                       
                                       )
        self.label_retorno.pack()
        

        # Inicinado classe e guardando pergunta/resposta em uma variavel



        # Botão enviar pergunta
        self.botao_pergunta = ttk.Button(self.janela,text="Enviar ao Zeca Piscineiro",
                                         padding=5,
                                         cursor="hand2",
                                         command=self.imprimir_resposta
                                         )
        self.botao_pergunta.pack(padx=10, pady=10)

        # Botao enviar pergunta mal educada
        self.botao_pergunta = ttk.Button(self.janela,text="Enviar ao Zeca Piscineiro",
                                         padding=5,
                                         cursor="hand2",
                                         command=self.imprimir_resposta
                                         )
        self.botao_pergunta.pack(padx=10, pady=10)
        
        
    def imprimir_resposta(self):
        self.label_retorno.config(state="normal")
        
        pergunta = self.campo_pergunta.get()
        resposta = self.chat.enviar_mensagem(mensagem=f"{pergunta}")
        self.label_retorno.insert(ttk.END, f"{resposta} \n \n \n")
        self.label_retorno.config(state="disabled")

            

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Gemini_Bot()
    janela_app = Janela_Bot()
    janela_app.run()
    