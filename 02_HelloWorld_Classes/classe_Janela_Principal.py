import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class Janela_Principal:
    """Classe para a criação da self.janela principal"""

    # todos o componentes (atributos) ficam dentro de init
    def __init__(self):
        #Criando self.janela e titulo.
        self.janela = ttk.Window(themename='solar')
        self.janela.title("Spotify")

        self.janela.geometry("1280x720+260+160") #Aumentando a tela
        self.janela.resizable(False, False) # Para nao deixar o usuario aumentar ou diminuir a tela
        self.janela.iconbitmap("02_HelloWorld_Classes/icons/spotify.ico")

        #texto  bom dia
        self.label_bomdia = ttk.Label(self.janela, text="Digite seu nome e receba um bom dia do incrivel BOM DIA 3000!",
                                font=("Verdana", 20) 
                                )
        self.label_bomdia = self.label_bomdia.pack()  
        
        # Campos de textos:
        self.campo_musica = ttk.Entry(self.janela) #Entry utilizamos para fazer uma entrada, no caso uma caixa de texto
        self.campo_musica.pack(pady=10) # pack seriamos para desenhar/carregar o elemento

        #Botoes
        self.botao_procurar = ttk.Button(self.janela, text="Procurar musica", command=self.acao)
        self.botao_procurar.pack()

        # Textos aviso
        self.label_aviso = ttk.Label(self.janela, 
                            font=("Arial", 19)
        )
        self.label_aviso.pack(pady=1, padx=300) # Label pack é para pegar a label e colocar em um widget, tipo compactar em uma widget

    # todos os metodos ficam em outra funcoes
    #Funcoes botoes

    def acao(self):
        """Está função pega o nome digitado na caixa de texto e deseja um bom dia!"""
        self.nome = self.campo_musica.get()
        self.label_aviso.config(text=f"Bom dia, {self.nome}")


        
    # Deixando self.janela em loop para nao fechar
    def run(self):
        """Inicia o loop para deixar a self.janela aberta"""
        self.janela.mainloop()

