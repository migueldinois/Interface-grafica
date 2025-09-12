# PESO/altura(m)2

import ttkbootstrap as ttk
import tkinter
from PIL import Image, ImageTk

class CalculatorIMC:
    def __init__(self):
        
        self.janela = ttk.Window(themename="superhero")
        self.janela.geometry("1280x720+260+160")
        self.janela.resizable(False, False)
        self.janela.title("Calculadora IMC")
        self.janela.iconbitmap("04_Bot_Alex/icons/professor.ico")

        # Texto 1

        self.texto1 = ttk.Label(text="CalculadoraIMC",
                                font=("Verdana", 20)).pack(padx=10, pady=10)
        
        self.textopeso = ttk.Label(self.janela, text="Digite seu peso: ")
        self.textopeso.pack()
        self.peso = ttk.Entry(self.janela)
        self.peso.pack(padx=5, pady=5)
        self.textoaltura = ttk.Label(self.janela, text="Digite sua altura: ")
        self.textoaltura.pack()
        self.altura = ttk.Entry(self.janela)
        self.altura.pack(padx=5, pady=5)

        self.botao = ttk.Button(text="Calcular",
                                padding=10, command=self.calcular_imc)
        self.botao.pack(padx=5, pady=5)
        
        self.resposta = ttk.Label(text="Valor do IMC: ")
        self.resposta.pack(padx=5, pady=5)

        
        self.categoria_imc = ttk.Label(self.janela, text="")
        self.categoria_imc.pack()

    def calcular_imc(self):
        """Função para calcular o imc de acordo com as respostas do usuario"""
        peso_pessoa = float(self.peso.get())
        altura_pessoa = float(self.altura.get())
        # Transformando altura em metross
        altura_metros = altura_pessoa / 100
        self.resultado_imc = peso_pessoa / (altura_metros ** 2)
        self.resposta.config(text=f"Valor do IMC: {self.resultado_imc:.2f}")
        self.determinar_categoria()
        self.categoria_imc.config(text=f"Você está {self.classificacao}")
    

    def determinar_categoria(self):
        """Função para determinar a categoria do peso da pessoa, obesidade, peso ideal e etc"""
        if self.resultado_imc < 18.5:
            self.classificacao = "Abaixo do Peso Normal"
        if self.resultado_imc >= 18.5 and self.resultado_imc <= 24.9:
            self.classificacao = "No Peso Normal"
        if self.resultado_imc >= 25.0 and self.resultado_imc <= 29.9:
            self.classificacao = "Em Excesso de peso"
        if self.resultado_imc >= 30.0 and self.resultado_imc <= 34.9:
            self.classificacao = "Com Obesidade Grau 1"
        if self.resultado_imc >= 35.0 and self.resultado_imc <= 39.9:
            self.classificacao = "Com Obesidade Grau 2"
        if self.resultado_imc >= 40.0:
            self.classificacao = "Com Obesidade Grau 3"
        
        return self.classificacao
    
    def imagem_categoria(self):
        self.imagem_abaixo_peso = Image.open("05_CalculadoraIMC/imagens/baixo_peso.png")
        self.imagem_peso_ideal = Image.open("05_CalculadoraIMC/imagens/peso_ideal.png")
        self.imagem_excesso_peso = Image.open()
        




    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = CalculatorIMC()
    app.run()