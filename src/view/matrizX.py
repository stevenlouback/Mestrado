import sys

sys.path.append("D:\Mestrado\Dissertacao\Mestrado\Mestrado\src\dao")
sys.path.append("D:\Mestrado\Dissertacao\Mestrado\Mestrado\src\metodos")

from DAOmatrizx import Matrizx
from pca import PCA
from tkinter import *

matrizPrincipal = []

class Matriz:
    def __init__(self, toplevel):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(toplevel)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(toplevel)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(toplevel)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container9 = Frame(toplevel)
        self.container9["pady"] = 15

        self.titulo = Label(self.container1, text="Informe os Dados do Modelo :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbIdModelo = Label(self.container2, text="Nº Modelo:", font=self.fonte, width=10)
        self.lbIdModelo.pack(side=LEFT)

        self.txtIdModelo = Entry(self.container2)
        self.txtIdModelo["width"] = 10
        self.txtIdModelo["font"] = self.fonte
        self.txtIdModelo.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarAmostraModelo
        self.btnBuscar.pack(side=RIGHT)

        self.btnPCA = Button(self.container3, text="PCA", font=self.fonte, width=10)
        self.btnPCA["command"] = self.testePCA
        self.btnPCA.pack(side=RIGHT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def buscarAmostraModelo(self):
        matrizX = Matrizx()

        idModelo = self.txtIdModelo.get()

        self.lblmsg["text"] = matrizX.selectMatrizXModelo(idModelo)

    def testePCA(self):
        pca = PCA()
        matrizX = Matrizx()
        idModelo = self.txtIdModelo.get()

        matrizPrincipal = matrizX.selectMatrizXModeloMMM(idModelo)

        pca.testePCA(matrizPrincipal)


root = Tk()
Matriz(root)
root.mainloop()