import tkinter as tk    

#Criando janela e titulo.
janela = tk.Tk()
janela.title = ("Painel Profissional")

#Aumentando a tela
janela.geometry("1280x720+260+160")

# Para nao deixar o usuario aumentar ou diminuir a tela
janela.resizable(False, False)

#Mudar cor do fundo
janela.configure(bg="#FF0E0F")

label = tk.Label(janela, text="Hello World")
label.pack() # Label pack é para pegar a label e colocar em um widget, tipo compactar em uma widget

# Deixando janela em loop para nao fechar
janela.mainloop()