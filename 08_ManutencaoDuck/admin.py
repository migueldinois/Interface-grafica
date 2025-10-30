import ttkbootstrap as ttk
import sqlite3
import random

class admin:
    def __init__(self):
        self.janela = ttk.Window(themename="cyborg")
        self.janela.title("Administração")
        self.janela.geometry("1280x720+260+160")

        def run(self):
            self.janela.mainloop()


if __name__