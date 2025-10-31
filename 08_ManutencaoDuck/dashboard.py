import ttkbootstrap as ttk
import sqlite3
import random
from tkinter import messagebox

class DuckManutencao:
    def __init__(self):
        # Configurações gerais
        self.janela = ttk.Window(themename="vapor")
        self.janela.title("Sistema de Log de Manutenção de Ducks")
        self.janela.geometry("1280x720+260+160")

        # Título principal
        titulo = ttk.Label(
            self.janela,
            text="Log de Manutenção Duck",
            font=("Verdana", 24),
            padding=20,
        )
        titulo.pack(side="top")

        # Criando frame para TreeViews
        self.frame_treeview = ttk.Frame(self.janela)
        self.frame_treeview.pack(pady=20, fill="both", expand=True)

        # Criando frame para os botões
        self.frame_botoes = ttk.Frame(self.janela)
        self.frame_botoes.pack(side="bottom", pady=20)

        # Criando frame para o formulário
        self.frame_formulario = ttk.Frame(self.janela)
        self.frame_formulario.pack(side="bottom", pady=10)

        # Criando frame agora para adicionar coisas na servicos
        self.frame_servicos = ttk.Frame(self.janela)
        self.frame_servicos.pack(side="bottom", pady=10)


        # Marca campo
        ttk.Label(self.frame_formulario, text="Marca:", font=("Verdana", 12)).pack(padx=5, side="left")
        self.marca_resposta = ttk.Entry(self.frame_formulario, width=20)
        self.marca_resposta.pack(pady=5, padx=5, side="left")


        # Modelo campo
        ttk.Label(self.frame_formulario, text="Modelo:", font=("Verdana", 12)).pack(padx=5, side="left")
        self.modelo_resposta = ttk.Entry(self.frame_formulario, width=20)
        self.modelo_resposta.pack(pady=5, padx=5, side="left")

        # Ano campo
        ttk.Label(self.frame_formulario, text="Ano:", font=("Verdana", 12)).pack(padx=5, side="left")
        self.ano_resposta = ttk.Entry(self.frame_formulario, width=20)
        self.ano_resposta.pack(pady=5, padx=5, side="left")

        # Botões de ação
        self.adicionar_botao = ttk.Button(
            self.frame_botoes,
            text="Adicionar Carro",
            command=self.adicionar_carro,
            style="success",
        )
        self.adicionar_botao.pack(pady=10, padx=10, side="left")

        self.deletar_botao = ttk.Button(
            self.frame_botoes,
            text="Deletar Carro",
            command=self.deletar_carro,
            style="danger",
        )
        self.deletar_botao.pack(pady=10, padx=10, side="right")

        self.alterar_botao = ttk.Button(self.frame_botoes,
                                        text="Alterar Carro",
                                        style="primary",
                                        command=self.alterar_funcao)
        self.alterar_botao.pack(pady=10, padx=10, side="right")



        


        # Configurando TreeView de carros
        self.carros = ttk.Treeview(
            self.frame_treeview,
            columns=("matricula", "marca", "modelo", "ano"),
            show="headings",
            height=10,
            style="primary"
        )
        self.carros.pack(padx=10, pady=10, side="left", fill="both", expand=True)

        # Configurando cabeçalhos do TreeView de carros
        self.carros.heading("matricula", text="Matrícula")
        self.carros.heading("marca", text="Marca")
        self.carros.heading("modelo", text="Modelo")
        self.carros.heading("ano", text="Ano")

        self.carros.column("matricula", width=150, anchor="center")
        self.carros.column("marca", width=150, anchor="center")
        self.carros.column("modelo", width=150, anchor="center")
        self.carros.column("ano", width=150, anchor="center")

        # Configurando TreeView de serviços
        self.servicos = ttk.Treeview(
            self.frame_treeview,
            columns=("servico", "data", "custo"),
            show="headings",
            height=10,
            style="primary"
        )
        self.servicos.pack(padx=10, pady=10, side="right", fill="both", expand=True)

        # Configurando cabeçalhos do TreeView de serviços
        self.servicos.heading("servico", text="Serviço")
        self.servicos.heading("data", text="Data")
        self.servicos.heading("custo", text="Custo")

        self.servicos.column("servico", width=300, anchor="center")
        self.servicos.column("data", width=150, anchor="center")
        self.servicos.column("custo", width=150, anchor="center")


        # Conectando, criando cursor, e tambemm criando a tabela aqui


        conexao = sqlite3.connect("08_ManutencaoDuck/bd_manutencao_duck.sqlite")
        cursor = conexao.cursor()

        sql_tabela_carros = """CREATE TABLE IF NOT EXISTS carros(
                            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                            marca VARCHAR(50) NOT NULL,
                            modelo VARCHAR(50) NOT NULL,
                            ano varchar(4) NOT NULL)
                            """
        
        # executando
        cursor.execute(sql_tabela_carros)
         # atualizando lista
        self.atualizar_lista_carros()

        # salvando 
        conexao.commit()
       
        # e fechando o cursor
        cursor.close()
        conexao.close()



    def atualizar_lista_carros(self):
        """Atualiza a lista de carros no TreeView."""
        # se tiver dados ele vai deletar
        # esse get_children pega todos os itens do treeview
        for item in self.carros.get_children():
            self.carros.delete(item)
        
        # Conecta ao banco de dados
        conexao = sqlite3.connect("08_ManutencaoDuck/bd_manutencao_duck.sqlite")
        cursor = conexao.cursor()

        # Consulta os dados da tabela

        sql_atualizar_lista = """
            SELECT matricula, marca, modelo, ano FROM carros;
        """
        cursor.execute(sql_atualizar_lista)
        carros = cursor.fetchall()  # Armazena os resultados em uma variável local
        cursor.close()
        conexao.close()

        # Insere os dados no TreeView
        for linha in carros:
            self.carros.insert("", "end", values=linha)

    def alterar_funcao(self):
        """Funcao para alterar itens da lista de carros."""
        selecionado = self.carros.selection()
        if selecionado:
            # Pegando os novos coisas que vao ser alterada
            marca = self.marca_resposta.get()
            modelo = self.modelo_resposta.get()
            ano = self.ano_resposta.get()

            # verificando se os campos nao estao vazios
            if marca != None and modelo != None and ano != None:
                # Pegando a linha do carro que foi selecionado
                carro_id = self.carros.item(selecionado)["values"][0] # NAO ENTENDI ISSO MUITO BEM MAS esta funcionando

                # Atualizando no banco de dados
                conexao = sqlite3.connect("08_ManutencaoDuck/bd_manutencao_duck.sqlite")
                cursor = conexao.cursor()

                alterar_carro_sql = """
                    UPDATE carros
                    SET marca = ?, modelo = ?, ano = ?
                    WHERE matricula = ?
                """
                valores = [marca, modelo, ano, carro_id]
                cursor.execute(alterar_carro_sql, valores)
                conexao.commit()
                cursor.close()
                conexao.close()

                # Atualizando o TreeView
                self.atualizar_lista_carros()

                # Limpando os campos do formulário
                self.marca_resposta.delete(0, "end")
                self.modelo_resposta.delete(0, "end")
                self.ano_resposta.delete(0, "end")

            else:
                messagebox.showwarning("Aviso", "Você esqueceu de preencher algum campo")
        else:
            print("Selecione um carro para alterar.")


    def adicionar_carro(self):
        """Adiciona um carro ao TreeView e ao banco de dados."""
        marca = self.marca_resposta.get()
        modelo = self.modelo_resposta.get()
        ano = self.ano_resposta.get()

        if marca and modelo and ano:
            # Adiciona ao banco de dados
            conexao = sqlite3.connect("08_ManutencaoDuck/bd_manutencao_duck.sqlite")
            cursor = conexao.cursor()

            adicionar_carro_sql = """
                INSERT INTO carros(marca, modelo, ano)
                VALUES(?, ?, ?)
            """
            valores = [marca, modelo, ano]
            cursor.execute(adicionar_carro_sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()

            # Atualiza o TreeView
            self.atualizar_lista_carros()

            # Limpa os campos do formulário
            self.marca_resposta.delete(0, "end")
            self.modelo_resposta.delete(0, "end")
            self.ano_resposta.delete(0, "end")
        else:
            messagebox.showwarning("Aviso", "Você esqueceu de preencher algum campo")



    def deletar_carro(self):
        """Deleta o carro selecionado no TreeView."""
        selecionado = self.carros.selection()
        if selecionado != None:
            
            # Deleta do banco de dados
            # Pegando matricula do carro que foi selecionado
            carro_id = self.carros.item(selecionado)["values"][0]
            conexao = sqlite3.connect("08_ManutencaoDuck/bd_manutencao_duck.sqlite")
            cursor = conexao.cursor()
            deletar_carro_sql = """ DELETE FROM carros 
                                    WHERE matricula = ? 
                                        """
            
            valores = [carro_id]
            cursor.execute(deletar_carro_sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
            self.carros.delete(selecionado)
        else:
            print("Selecione um carro para deletar.")

        

    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = DuckManutencao()
    app.run()