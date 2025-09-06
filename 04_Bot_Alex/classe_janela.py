from classe_robo import Gemini_Bot
import ttkbootstrap as ttk

class Janela_Bot:
    def __init__(self):
        # Criando a janela em si
        self.janela = ttk.Window(themename="superhero")
        self.janela.title("Alex Professor")

        #Definindo icone, tamanho e impossibilitando para mexer na altura e largura
        self.janela.iconbitmap("04_Bot_Alex/icons/professor.ico")
        self.janela.geometry("1280x720+260+160")
        self.janela.resizable(False, False)

        #Criando textos principais 
        self.titulo1 = ttk.Label(text="Doutor_Piscinas",
                                 font=("Segoe UI", 20)
                                 )
        self.titulo1.pack(padx=10, pady=10)

        # Campo de pergunta

        self.campo_pergunta = ttk.Entry(width=50)
        self.campo_pergunta.pack(padx=10, pady=10)

        # RESPOSTA DA I.A
        self.label_retorno = ttk.Text(width=80,
                                       wrap="word"
                                       )
        self.label_retorno.pack()

        # Botão enviar pergunta
        pergunta = self.campo_pergunta.get()
        resposta = app.enviar_mensagem(mensagem=f"{pergunta}")
        self.botao_pergunta = ttk.Button(text="Pergunar ao Doutor Piscinas",
                                         padding=5,

                                         )
        self.botao_pergunta.pack(padx=10, pady=10)
        
        

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Gemini_Bot()
    janela_app = Janela_Bot()
    janela_app.run()
    