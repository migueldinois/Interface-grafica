import tkinter.messagebox
import ttkbootstrap as ttk
import tkinter
import json
import random
from tkinter import messagebox
from classe_lista_tarefas import ListaDeTarefas
import sqlite3

class Login:
    def __init__(self):
        
        self.janela = ttk.Window(themename="vapor")
        self.janela.protocol("WM_DELETE_WINDOW", self.quando_fechar)
        self.janela.iconbitmap("06_Lista_Tarefas/icons/icone.ico")
        self.janela.geometry("1280x720+260+160")
        self.janela.resizable(False, False)
        self.janela.title("Lista de Tarefas - Login")
        

        # Titulo Principal da janela de login
        texto_cadastro = ttk.Label(self.janela, text="Tela de Cadastro" \
        ",", font=("Segoe UI", 20))
        texto_cadastro.pack()

        descricao = ttk.Label(self.janela, text="Preencha as informacoes para cadastrar-se", font=("Verdana", 14), padding=10)
        descricao.pack()

        # Campos para colocar login e senha

        ttk.Label(self.janela, text="Nome:", font=("Verdana", 14), padding=3).pack()
        self.campo_nome = ttk.Entry(self.janela)
        self.campo_nome.pack(padx=10, pady=10)

        ttk.Label(self.janela, text="Usario:", font=("Verdana", 14), padding=3).pack()
        self.campo_usuario = ttk.Entry(self.janela)
        self.campo_usuario.pack(padx=10, pady=10)

        ttk.Label(self.janela, text="Senha:", font=("Verdana", 14), padding=3).pack()
        self.campo_senha = ttk.Entry(self.janela, show="*")                                                    
        self.campo_senha.pack(padx=10, pady=10)

        ttk.Label(self.janela, text="Sua senha novamente:", font=("Verdana", 14), padding=3).pack()
        self.campo_senha2 = ttk.Entry(self.janela, show="*")                                                    
        self.campo_senha2.pack(padx=10, pady=10)


        # Botoes de cancelar e logar

        frame_botao = ttk.Frame()
        frame_botao.pack()

        cadastro_botao = ttk.Button(frame_botao,text="Cadastrar-se",padding=10, command=self.cadastro_funcao).pack(side="left", padx=4, pady=10)

        cancelar_botao = ttk.Button(frame_botao,text="Cancelar", padding=10, command=self.exit).pack(side="right", padx=4)

        #Conectando ao banco de dados
        conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")

        #Criando responsavel por comandar o Banco de Dados 
        cursor = conexao.cursor()

        #Criando tabela 
        sql_para_criar_tabela = """
                                CREATE TABLE IF NOT EXISTS usuarios (
                                codigo integer primary key autoincrement,
                                nome varchar(80),
                                usuario varchar(24),
                                senha varchar(20)
                                );
                                """
        cursor.execute(sql_para_criar_tabela)

        # Confirma as alterações
        conexao.commit()
        
        #fechei a conexão
        cursor.close()
        conexao.close()

        self.atualizar_lista()

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





        
    def cadastro_funcao(self):
        self.resposta_nome = self.campo_nome.get()
        self.resposta_usuario = self.campo_usuario.get()
        self.resposta_senha = self.campo_senha.get()
        self.resposta_senha2 = self.campo_senha2.get()

        if self.resposta_senha == self.resposta_senha2:
            conexao = sqlite3.connect("06_lista_tarefas/bd_lista_tarefas.sqlite")
            cursor = conexao.cursor()

            sql_cadastrar_usuario = """
                INSERT INTO usuarios(nome, usuario, senha)
                VALUES(?, ?, ?)
                """
            
            valores = [self.resposta_nome, self.resposta_usuario, self.resposta_senha]

            cursor.execute(sql_cadastrar_usuario, valores)
            
            conexao.commit()

            messagebox.showinfo(message="você foi cadastrado!")
            cursor.close()
            conexao.close()
            
        else:
            messagebox.showerror(message="Suas senhas não são iguais! ")

    

    def exit(self):
        exit()
        
    def quando_fechar(self):
        if messagebox.askyesno("Aviso", "Deseja fechar o Aplicativo?") == True:
            exit()

    def run(self):
        self.janela.mainloop()
        

if __name__ == "__main__":    
    app = Login()
    app.run()