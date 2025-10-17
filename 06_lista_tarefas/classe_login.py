import tkinter.messagebox
import ttkbootstrap as ttk
import tkinter
import json
import random
from tkinter import messagebox


class Login:
    def __init__(self, janelaPai):
        
        self.janela = ttk.Toplevel(janelaPai)

        # Configurando para que quando feche a janela de login ele feche o programa!


        self.janela.protocol("WM_DELETE_WINDOW", self.quando_fechar)
        self.janela.iconbitmap("06_Lista_Tarefas/icons/icone.ico")
        self.janela.geometry("1280x720+260+160")
        self.janela.resizable(False, False)
        self.janela.title("Lista de Tarefas - Login")
        

        # Titulo Principal da janela de login
        bemVindo = ttk.Label(self.janela, text="Bem vindo!" \
        ",", font=("Segoe UI", 20))
        bemVindo.pack()

        loginContinue = ttk.Label(self.janela, text="Faça login para continuar:", font=("Verdana", 14), padding=10)
        loginContinue.pack()

        # Campos para colocar login e senha

        self.campo_usuario = ttk.Entry(self.janela)
        self.campo_usuario.pack(padx=10, pady=10)

        self.campo_senha = ttk.Entry(self.janela, show="*")                                                    
        self.campo_senha.pack()

        # Botoes de cancelar e logar

        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack()

        logar_botao = ttk.Button(frame_botao,text="Logar",padding=10, command=self.logar_funcao).pack(side="left", padx=4, pady=10)



        cancelar_botao = ttk.Button(frame_botao,text="Cancelar", padding=10, command=self.exit).pack(side="right", padx=4)
 
 

        
    def logar_funcao(self):
        self.resposta_usuario = self.campo_usuario.get()
        self.resposta_senha = self.campo_senha.get()

        if self.resposta_usuario == "1" and self.resposta_senha == "1":
            tkinter.messagebox.showinfo("Logado com sucesso!", "Aproveite o melhor aplicativo do mundo!")
            self.janela.destroy()
            tela_lista = ListaDeTarefas()
            tela_lista.run()


        else:
            tkinter.messagebox.showerror("Aviso!", "Seu login não existe ou está errado!")  

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
    