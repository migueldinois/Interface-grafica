# PESO/altura(m)2

import ttkbootstrap as ttk
import tkinter.messagebox
from PIL import Image, ImageTk

class CalculatorIMC:
    def __init__(self):
        
        self.janela = ttk.Window(themename="morph")
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
        self.textoaltura = ttk.Label(self.janela, text="Digite sua altura (Céntimetros): ")
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

        # COlocando fotos para cada tipo de peso


        self.imagem_classificada = ttk.Label(self.janela, image="")
        self.imagem_classificada.pack()

    def calcular_imc(self):
        """Função para calcular o imc de acordo com as respostas do usuario"""
        self.verificar_campos()
        if self.verificado_altura == "1" and self.verificado_peso == "1":
            peso_pessoa = self.peso.get()
            altura_pessoa = self.altura.get()
            # Calculando IMC
            altura_metros = float(altura_pessoa) / 100
            self.resultado_imc = float(peso_pessoa) / (float(altura_metros) ** 2)
            self.resposta.config(text=f"Valor do IMC: {self.resultado_imc:.2f}")

            # Determinando classificacao dela
            self.determinar_categoria()
            self.categoria_imc.config(text=f"Você está {self.classificacao}")

            self.imagem_mostrar = "Imagem indi"
            if self.classificacao == "Abaixo do Peso Normal":
                self.imagem_mostrar = self.imagem1
            if self.classificacao == "No Peso Normal":
                self.imagem_mostrar = self.imagem2
            if self.classificacao == "Em Excesso de peso":
                self.imagem_mostrar = self.imagem3
            if self.classificacao == "Com Obesidade Grau 1":
                self.imagem_mostrar = self.imagem4
            if self.classificacao == "Com Obesidade Grau 2":
                self.imagem_mostrar = self.imagem5
            if self.classificacao == "Com Obesidade Grau 3":
                self.imagem_mostrar = self.imagem6

            self.imagem_classificada.config(image=self.imagem_mostrar)
        
    def verificar_campos(self):
        self.peso_entry = self.peso.get()
        self.altura_entry = self.altura.get()
        self.verificado_peso = "1"
        self.verificado_altura = "1"
        
        if self.peso_entry == "":
            tkinter.messagebox.showwarning("Atenção!","Insira seu peso")
            self.verificado_peso = "0"
        if self.altura_entry == "":
            tkinter.messagebox.showwarning("Atenção!","Insira sua altura")
            self.verificado_altura = "0"

        
    

    def determinar_categoria(self):
        """Função para determinar a categoria do peso da pessoa, obesidade, peso ideal e etc"""

        # Abrindo Imagens e carregando imagens
        self.imagem_abaixo_peso = Image.open("05_CalculadoraIMC/imagens/baixo_peso.png")
        self.imagem_peso_ideal = Image.open("05_CalculadoraIMC/imagens/peso_ideal.png")
        self.imagem_excesso_peso = Image.open("05_CalculadoraIMC/imagens/excesso_peso.png")
        self.imagem_obesidade_grauI = Image.open("05_CalculadoraIMC/imagens/Obesidade_grau1.png")
        self.imagem_obesidade_grauII = Image.open("05_CalculadoraIMC/imagens/Obesidade_grau2.png")
        self.imagem_obesidade_grauIII = Image.open("05_CalculadoraIMC/imagens/Obesidade_grau3.png")

        self.imagem1 = ImageTk.PhotoImage(self.imagem_abaixo_peso)
        self.imagem2 = ImageTk.PhotoImage(self.imagem_peso_ideal)
        self.imagem3 = ImageTk.PhotoImage(self.imagem_excesso_peso)
        self.imagem4 = ImageTk.PhotoImage(self.imagem_obesidade_grauI)
        self.imagem5 = ImageTk.PhotoImage(self.imagem_obesidade_grauII)
        self.imagem6 = ImageTk.PhotoImage(self.imagem_obesidade_grauIII)



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
        

        
        




    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = CalculatorIMC()
    app.run()