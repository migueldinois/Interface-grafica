# PESO/altura(m)2

import ttkbootstrap as ttk
import tkinter

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
        
        self.peso = ttk.Entry(self.janela)
        self.peso.pack(padx=5, pady=5)
        self.altura = ttk.Entry(self.janela)
        self.altura.pack(padx=5, pady=5)

        self.botao = ttk.Button(text="Calcular",
                                padding=10, command=self.calcular_imc)
        self.botao.pack(padx=5, pady=5)
        
        self.resposta = ttk.Label(text="Valor do IMC: ")
        self.resposta.pack(padx=5, pady=5)

    def calcular_imc(self):
        peso_pessoa = self.peso.get()
        altura_pessoa = self.altura.get()
        altura_dobrada = altura_pessoa * 2
        resultado_imc = float(peso_pessoa) / float(altura_dobrada)
        self.resposta.config(text=resultado_imc) 



    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = CalculatorIMC()
    app.run()