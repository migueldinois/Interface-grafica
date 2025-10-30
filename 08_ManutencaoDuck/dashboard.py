import ttkbootstrap as ttk
import sqlite3
import random



class DuckManutencao:
    def __init__(self):
        
        # Configuracoes gerais
        self.janela = ttk.Window(themename="vapor")
        self.janela.title("Sistema de Log de Manutenção de Ducks")
        self.janela.geometry("1280x720+260+160")

        # Titulos
        titulo = ttk.Label(self.janela, text="Log Manutenção ",
                            font=("Verdana", 20), 
                            padding=10, )
        titulo.pack(side="top", fill="x")

        
        # Criando frame das tree view
        self.frame_treeview = ttk.Frame(self.janela)
        self.frame_treeview.pack(pady=10)
        
        # Criando um frame para os botoes e os campo de texto
        self.frame_formularo = ttk.Frame(self.janela)
        self.frame_formularo.pack(pady=10, side="left", padx=20)

        # frame para botoes
        self.frame_botoes = ttk.Frame(self.janela)
        self.frame_botoes.pack(pady=10, side="right", padx=20)

        # Criando botoes para eu conseguir deletar, adicionar e etc
        # entry para marca
        titulo_ano = ttk.Label(self.frame_formularo ,text="Marca:").pack(padx=5, side="left")
        self.marca_resposta = ttk.Entry(self.frame_formularo, width=20)
        self.marca_resposta.pack(pady=5, padx=5, side="left")

        # entry para modelo
        titulo_ano = ttk.Label(self.frame_formularo ,text="Modelo:").pack(padx=5, side="left")
        self.modelo_resposta = ttk.Entry(self.frame_formularo, width=20)
        self.modelo_resposta.pack(pady=5, padx=5, side="left")

        # entry para ano
        titulo_ano = ttk.Label(self.frame_formularo ,text="Ano:").pack(padx=5, side="left")
        self.ano_resposta = ttk.Entry(self.frame_formularo, width=20)
        self.ano_resposta.pack(pady=5, padx=5, side="left")

        # botao para adicionar carro
        self.adicionar_botao = ttk.Button(self.frame_formularo, text="Adicionar Carro", command=self.adicionar_carro)
        self.adicionar_botao.pack(pady=10, padx=5, side="left")

        # botao para deletar carro
        self.deletar_botao = ttk.Button(self.frame_formularo, text="Deletar Carro", command=self.deletar_carro)
        self.deletar_botao.pack(pady=10,padx=5, side="left")

        

        


        # Configurando o primeiro Tree View que é o de carros
        self.carros = ttk.Treeview(self.frame_treeview, columns=("matricula", "marca", "modelo", "ano"), show="headings")

        # Fill para preencher tudo o espaço e expand para se o cara aumentar ou diminur vai tambem aumentar ou diminuir
        self.carros.pack(padx=10, pady=10, side="left")

        # Criando os headers
        self.carros.heading("matricula", text="Matrícula")
        self.carros.heading("marca", text="Marca")
        self.carros.heading("modelo", text="Modelo")
        self.carros.heading("ano", text="Ano")

        self.carros.column("matricula", width=150, anchor="center")
        self.carros.column("marca", width=150, anchor="center")
        self.carros.column("modelo", width=150, anchor="center")
        self.carros.column("ano", width=150, anchor="center")


        # Configurando segundo tree view que é o de servicos
        
        self.servicos = ttk.Treeview(self.frame_treeview, columns=("servico", "data", "custo"), show="headings")
        self.servicos.pack(padx=10, pady=10, side="right")

        # Criando o header
        self.servicos.heading("servico", text="Serviço")
        self.servicos.heading("data", text="Data")
        self.servicos.heading("custo", text="Custo")
        
        self.servicos.column("servico", width=300, anchor="center")
        self.servicos.column("data", width=150, anchor="center")
        self.servicos.column("custo", width=150, anchor="center")




    def adicionar_carro(self):
        self_resposta_marca = self.marca_resposta.get(),
        self.resposta_modelo = self.modelo_resposta.get(),
        self.resposta_ano = self.ano_resposta.get()

    
        """Adiciona um carro ao Tree View com os dados que o cara prencheu nas entradas."""
        self.carros.insert("", "end", values=(
            random.randint(1000, 9999),

        ))


    def deletar_carro(self):
        """Deleta o carro selecionado."""
        self.carros.delete(self.carros.selection())


        
        

    def run(self):
        self.janela.mainloop()



if __name__ == "__main__":
    app = DuckManutencao()
    app.run()