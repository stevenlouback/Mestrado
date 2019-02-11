from tkinter import *
from amostra import Amostra


class TelaPrincipal(Frame):
    def __init__(self, toplevel):
        Frame.__init__(self, toplevel)

        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Abrir!', background='green')
        self.botao.bind("<Button-1>", self.abre)
        self.botao.pack()

    def abre(self, event):
        r = Tk()
        amostra = Amostra()
        amostra.Amostra(r)
        r.mainloop()

raiz = Tk()
TelaPrincipal(raiz)
raiz.mainloop()

