import tkinter.messagebox
import ttkbootstrap as ttk
import tkinter
import json
import sqlite3
import random
from tkinter import messagebox
from classe_login import Login


class ListaDeTarefas:
    def __init__(self, usuario_logado=None):
        self.usuario_logado = usuario_logado

        self.janela = ttk.Window(themename="vapor")
        self.janela.iconbitmap("06_lista_tarefas/icons/icone.ico")
        self.janela.geometry("820x720+260+160")
        self.janela.title("Lista de Tarefas")

        # Titulo Principal da lista
        titulo = ttk.Label(self.janela, text="Lista de Tarefas", font=("Verdana", 20), padding=5)
        titulo.pack(pady=30)

        # Descricao do app
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

        # Conectando ao banco de dados
        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        # Criando tabela 
        sql_para_criar_tabela = """
            CREATE TABLE IF NOT EXISTS tarefa (
                codigo integer primary key autoincrement,
                usuario varchar(15),
                descricao_tarefa varchar(200),
                FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
            );
        """
        cursor.execute(sql_para_criar_tabela)
        conexao.commit()
        cursor.close()
        conexao.close()

        self.atualizar_lista()

        Login(self)
        self.janela.withdraw()

    def atualizar_lista(self):
        self.lista_tarefas.delete(0, "end")  # Limpa a lista atual
        
        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        sql_para_selecionar_tarefas = """
            SELECT codigo, descricao_tarefa 
            FROM tarefa 
            WHERE usuario = ?;
        """
        cursor.execute(sql_para_selecionar_tarefas, [self.usuario_logado])
        lista_de_tarefas = cursor.fetchall()
        cursor.close()
        conexao.close()

        for linha in lista_de_tarefas:
            self.lista_tarefas.insert("end", linha[1])

    def add_tarefa(self):
        tarefa = self.tarefa.get()
        
        if not tarefa.strip():
            messagebox.showerror("Erro", "A tarefa não pode estar vazia!")
            return

        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        sql_insert = """
            INSERT INTO tarefa (usuario, descricao_tarefa)
            VALUES (?, ?)
        """
        cursor.execute(sql_insert, [self.usuario_logado, tarefa])
        conexao.commit()
        cursor.close()
        conexao.close()

        self.lista_tarefas.insert(0, tarefa)
        self.tarefa.delete(0, "end")  # Limpa o campo após adicionar

    def remove_tarefa(self):
        item_indice = self.lista_tarefas.curselection()

        if item_indice:
            texto_indice = self.lista_tarefas.get(item_indice)
            self.lista_tarefas.delete(item_indice)

            conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
            cursor = conexao.cursor()

            sql_delete = """
                DELETE FROM tarefa 
                WHERE descricao_tarefa = ? AND usuario = ?;
            """
            cursor.execute(sql_delete, [texto_indice, self.usuario_logado])
            conexao.commit()
            conexao.close()
        else:
            messagebox.showerror(message="Selecione um item antes de excluir")

    def marcar_concluido(self):
        item_selecionada = self.lista_tarefas.curselection()

        if item_selecionada:
            texto_tarefa = self.lista_tarefas.get(item_selecionada)

            if "[CONCLUIDO]" not in texto_tarefa:
                self.lista_tarefas.delete(item_selecionada[0])
                texto_tarefa_concluido = texto_tarefa + " [CONCLUIDO]"
                self.lista_tarefas.insert(item_selecionada[0], texto_tarefa_concluido)

                with sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite") as conexao:
                    cursor = conexao.cursor()

                    sql_update = """
                        UPDATE tarefa
                        SET descricao_tarefa = ?
                        WHERE descricao_tarefa = ? AND usuario = ?;
                    """
                    valores = (texto_tarefa_concluido, texto_tarefa, self.usuario_logado)
                    cursor.execute(sql_update, valores)
        else:
            messagebox.showerror("Aviso", "Selecione uma tarefa para concluir.")

    

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = ListaDeTarefas()
    app.run()