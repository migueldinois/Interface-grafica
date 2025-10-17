
import tkinter.messagebox
import ttkbootstrap as ttk
import tkinter
import json
import sqlite3
import random
from tkinter import messagebox
from classe_login import Login


class ListaDeTarefas:


    def __init__(self):

        self.janela = ttk.Window(themename="vapor")
        self.janela.iconbitmap("06_lista_tarefas/icons/icone.ico")
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



         #Conectando ao banco de dados
        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")

        #Criando responsavel por comandar o Banco de Dados 
        cursor = conexao.cursor()

        #Criando tabela 
        sql_para_criar_tabela = """
                                CREATE TABLE IF NOT EXISTS tarefa (
                                codigo integer primary key autoincrement,
                                descricao_tarefa varchar(200)
                                );
                                """
        cursor.execute(sql_para_criar_tabela)

        # Confirma as alterações
        conexao.commit()
        
        #fechei a conexão
        cursor.close()
        conexao.close()

        self.atualizar_lista()


        Login(self.janela)
        # Esconedendo a janela de tarefas
        self.janela.withdraw()

    def atualizar_lista(self):

        #atualizar tarefa 

        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        sql_para_selecionar_tarefas = """
                                        select codigo, descricao_tarefa from tarefa;
                                        """
        cursor.execute(sql_para_selecionar_tarefas)

        lista_de_tarefas =cursor.fetchall()

        cursor.close()
        conexao.close()

        #inserindo items listbox
        for linha in lista_de_tarefas:
            self.lista_tarefas.insert("end", linha[1])









    # Funcao para adicionar tarefa a lista


    def add_tarefa(self):
        #pegango o texto da caixa de texto
        tarefa = self.tarefa.get()

        self.lista_tarefas.insert(0, tarefa)

        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        sql_insert = """
                        INSERT INTO tarefa (descricao_tarefa)
                        VALUES (?)
                    """
        cursor.execute(sql_insert,[tarefa])
        conexao.commit()

        cursor.close()
        conexao.close()

    def remove_tarefa(self):
        item_indice = self.lista_tarefas.curselection()
        


        if item_indice:
            texto_indice = self.lista_tarefas.get(item_indice)
            
            self.lista_tarefas.delete(item_indice)

            conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
            cursor = conexao.cursor()

            sql_delete = """
                            DELETE FROM tarefa 
                            WHERE descricao_tarefa = ?;

                        """
            
            
            
            cursor.execute(sql_delete, [texto_indice])
            conexao.commit()
            conexao.close()
            



        else:
            messagebox.showerror(message="Selecione um item antes de excluir")

    def marcar_concluido(self):
        item_selecionada = self.lista_tarefas.curselection()

        if item_selecionada:
            texto_tarefa = self.lista_tarefas.get(item_selecionada)


            # Vendo se o texto da tarefa nao esta CONCLUIDO pois nao pode conckluir duas vezes
            if "[CONCLUIDO]" not in texto_tarefa:
                
                #Mexendo na      visual do app, para o usuario ver, no caso a lista e nao o banco de dados
                self.lista_tarefas.delete(item_selecionada[0]) 
                texto_tarefa_concluido = texto_tarefa + " [CONCLUIDO]" 
                self.lista_tarefas.insert(item_selecionada[0], texto_tarefa_concluido)

                # COnectando mesmo se der erro
                with sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite") as conexao:
                    cursor = conexao.cursor()

                    sql_update = """
                                UPDATE tarefa
                                SET descricao_tarefa = ?
                                WHERE descricao_tarefa = ?;
                                """
                    
                    # Esses valores eu coloquei para usar como variavel dentro do codigo, é ordem respectivamente, como o 
                    # texto_tarefa_concluido fica primeiro e é trocado no SET da descricao e o texto_tarefa é para o where
                    valores = (texto_tarefa_concluido, texto_tarefa)
                    
                    # Aqui executamos o sql junto com os valores
                    cursor.execute(sql_update, valores)
                    

        else:
            messagebox.showerror("Aviso", "Selecione uma tarefa para concluir.")

    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    app = ListaDeTarefas()
    app.run()