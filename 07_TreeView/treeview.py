import ttkbootstrap as ttk

# Criando a janela principal
janela = ttk.Window(themename="cosmo")
janela.title("Exemplo Treeview")

# Configurando o Treeview
tree = ttk.Treeview(janela, columns=("nome", "idade"), show="headings")
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Definindo os Header

tree.heading("nome", text="Nome")
tree.heading("idade", text="Idade")

# Configurando a largura das colunas e outras coisas8
tree.column("nome", width=150, anchor="center")
tree.column("idade", width=80, anchor="center")

# Inserindo alguns dados de exemplo
dados = [("Ana", 25), ("Bruno", 30), ("Carla", 28)]

# Adicionando os dados ao Treeview nome é a primeira e depois idade e ele vai adicionando, enquanto tiver nomes ele vai adicionar ao final
for nome, idade in dados:
	tree.insert("", "end", values=(nome, idade))

# funcao de pegar dados e printar


def apagar_item():
    item_selecionado = tree.selection()
    for item in item_selecionado:
        tree.delete(item)

botao_apagar = ttk.Button(janela, text="Apagar Selecionado", command=apagar_item).pack(pady=10)

janela.mainloop()