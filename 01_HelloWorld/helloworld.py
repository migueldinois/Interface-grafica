import tkinter as tk    

#Criando janela e titulo.
janela = tk.Tk()
janela.title = ("Painel Profissional")


label = tk.Label(janela, text="Hello World")
label.pack() # Label pack é para pegar a label e colocar em um widget, tipo compactar em uma widget

# Deixando janela em loop para nao fechar
janela.mainloop()