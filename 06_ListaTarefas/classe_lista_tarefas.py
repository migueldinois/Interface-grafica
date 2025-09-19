
import tkinter.messagebox
import ttkbootstrap as ttk
import tkinter
import json
import random
from tkinter import messagebox


class ListaDeTarefas:

    

    def __init__(self):
        self.janela = ttk.Window(themename="vapor")
        self.janela.iconbitmap("06_ListaTarefas/icons/icone.ico")
        self.janela.geometry("1280x720+260+160")
        self.janela.resizable(False, False)
        self.janela.title("Lista de Tarefas")

    # Titulo Principal da lista

        titulo = ttk.Label(self.janela, text="Lista de Tarefas", font=("Verdana", 20), padding=5)
        titulo.pack(pady=30)

    #  Descricao do app
        descricao = ttk.Label(self.janela, text="Seja organizado e utilize ese app para te ajudar no dia a dia!", font=("Verdana", 15), padding=10)
        descricao.pack()

    # Campo de escrever e adcionar tarefa 

        self.tarefa = ttk.Entry(self.janela, width=100)
        self.tarefa.pack(pady=40)
    
        logar_botao = ttk.Button(text="Adicionar Tarefa",padding=5, command=self.add_tarefa)
        logar_botao.pack(pady=20)
        logar_botao.place(x=535, y=230)

        cancelar_botao = ttk.Button(text="Remover Tarefa", padding=5)
        cancelar_botao.pack(pady=20)
        cancelar_botao.place(x=650, y= 230) 

    # Campo para listar as tarefas
        self.lista_tarefas = tkinter.Listbox(state="disabled", width=100)
        self.lista_tarefas.pack()


    # Funcao para adicionar tarefa a lista

    def add_tarefa(self):
        self.lista_tarefas.config(state="normal")
        # Pegar o texto do entryu
        self.tarefa_texto = self.tarefa.get()
        # Salvar a lista inteira no dicionario
        tkinter.messagebox.showinfo("Tarefa Adicionada", f"A tarefa {self.tarefa_texto} foi adicionada a lista de tarefas!")

        self.lista_tarefas.insert(ttk.END, f"{self.tarefa_texto} \n")
        self.lista_tarefas.config(state="disabled")




    def run(self):
        self.janela.mainloop()


    

if __name__ == "__main__":
    app = ListaDeTarefas()
    app.run()