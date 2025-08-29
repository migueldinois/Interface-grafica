import tkinter as tk    

#Criando janela e titulo.
janela = tk.Tk()
janela.title("Spotify")

janela.geometry("1280x720+260+160")#Aumentando a tela
janela.resizable(False, False) # Para nao deixar o usuario aumentar ou diminuir a tela
janela.iconbitmap("01_HelloWorld/icons/spotify.ico")
janela.configure(bg="#1DB954")#Mudar cor do fundo

#Funcoes botoes

def acao():
    """Está função pega o nome digitado na caixa de texto e deseja um bom dia!"""
    nome = campo_musica.get()
    label_aviso.config(text=f"Bom dia, {nome}")

#texto  bom dia
label_bomdia = tk.Label(janela, text="Digite seu nome e receba um bom dia do incrivel BOM DIA 3000!",
                        bg="#49be25",
                        font=("Verdana", 20) 
                        )
label_bomdia = label_bomdia.pack()  



# Campos de textos:

campo_musica = tk.Entry(janela) #Entry utilizamos para fazer uma entrada, no caso uma caixa de texto
campo_musica.pack(pady=10) # pack seriamos para desenhar/carregar o elemento

#Botoes
botao_procurar = tk.Button(janela, text="Procurar musica", command=acao, padx=20)
botao_procurar.pack()

# Textos aviso
label_aviso = tk.Label(janela, bg="#43fb2d",
                       font=("Arial", 19)
)
label_aviso.pack(pady=1, padx=300) # Label pack é para pegar a label e colocar em um widget, tipo compactar em uma widget

# Deixando janela em loop para nao fechar
janela.mainloop()