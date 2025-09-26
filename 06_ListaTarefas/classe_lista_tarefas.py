
import tkinter.messagebox
import ttkbootstrap as ttk
import tkinter
import json
import sqlite3
import random
from tkinter import messagebox


class ListaDeTarefas:

    

    def __init__(self):



        # conectando ao banco de dados
        bancodedados = sqlite3.connect("banco_de_dados.db")
        cursor = bancodedados.cursor()

        # #Criando a tabela  
        # cursor.execute('''CREATE TABLE Tarefas
        #                (ID_TAREFA INT, 
        #                NOME_TAREFA VARCHAR(50) NOT NULL
        #                )''')

        # #Exibindo os dados do banco dentro da caixa de texto

        # # Colocando dados test
        # cursor.execute("INSERT INTO Tarefas values (?, ?)", ("C", 1972))


        self.janela = ttk.Window(themename="vapor")
        self.janela.iconbitmap("06_ListaTarefas/icons/icone.ico")
        self.janela.geometry("820x720+260+160")
        self.janela.title("Lista de Tarefas")

    # Titulo Principal da lista

        titulo = ttk.Label(self.janela, text="Lista de Tarefas", font=("Verdana", 20), padding=5)
        titulo.pack(pady=30)

    #  Descricao do app
        descricao = ttk.Label(self.janela, text="Seja organizado e utilize ese app para te ajudar no dia a dia!", font=("Verdana", 15), padding=10)
        descricao.pack()

    # Campo de escrever e adcionar tarefa 

        frame_botoes = ttk.Frame()
        frame_botoes.pack(pady=10)

        self.tarefa = ttk.Entry(frame_botoes, width=100)
        self.tarefa.pack(side="left",fill="x", expand=True)


    
        add_tarefa = ttk.Button(frame_botoes, text="Adicionar Tarefa", command=self.add_tarefa)
        add_tarefa.pack(side="right", padx=10, fill="x", expand=True)



    # Campo para listar as tarefas
        self.lista_tarefas = tkinter.Listbox(state="normal", width=120, height=25)
        self.lista_tarefas.pack()

        frame_baixo = ttk.Frame(self.janela)
        frame_baixo.pack(expand=True)

        cancelar_botao = ttk.Button(frame_baixo, text="Remover Tarefa", cursor="hand2", style="danger", command=self.remove_tarefa)
        cancelar_botao.pack(side="right", expand=True, padx=10)

        concluir_botao = ttk.Button(frame_baixo, text="Concluir Tarefa", cursor="hand2", style="sucess", command=self.marcar_concluido)
        concluir_botao.pack(side="left", expand=True)

    # Funcao para adicionar tarefa a lista

    def add_tarefa(self):
        # Pegar o texto do entryu
        self.tarefa_texto = self.tarefa.get()
        # Salvar a lista inteira no dicionario
        tkinter.messagebox.showinfo("Tarefa Adicionada", f"A tarefa {self.tarefa_texto} foi adicionada a lista de tarefas!")

        # Adicionando um texto no final campo
        self.lista_tarefas.insert(ttk.END, f"{self.tarefa_texto} \n")

    def remove_tarefa(self):
        tarefa_selecionada = self.lista_tarefas.curselection()
        self.lista_tarefas.delete(tarefa_selecionada[0])

    def marcar_concluido(self):
        tarefa_selecionada = self.lista_tarefas.curselection()
        self.lista_tarefas.itemconfig(tarefa_selecionada, {"fg": "green", "selectforeground": "green"})

    def run(self):
        self.janela.mainloop()


    

if __name__ == "__main__":
    app = ListaDeTarefas()
    app.run()