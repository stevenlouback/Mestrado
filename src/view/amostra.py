import sys

sys.path.append("D:\Mestrado\Dissertacao\Mestrado\Mestrado\src\dao")

from DAOamostra import Amostra
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados da Amostra :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbIdAmostra = Label(self.container2, text="Nº Amostra:", font=self.fonte, width=10)
        self.lbIdAmostra.pack(side=LEFT)

        self.txtIdAmostra = Entry(self.container2)
        self.txtIdAmostra["width"] = 10
        self.txtIdAmostra["font"] = self.fonte
        self.txtIdAmostra.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarAmostra
        self.btnBuscar.pack(side=RIGHT)

        self.lbDtColetaAmostra = Label(self.container3, text="Data Coleta:", font=self.fonte, width=10)
        self.lbDtColetaAmostra.pack(side=LEFT)

        self.txtDtColetaAmostra = Entry(self.container3)
        self.txtDtColetaAmostra["width"] = 25
        self.txtDtColetaAmostra["font"] = self.fonte
        self.txtDtColetaAmostra.pack(side=LEFT)

        self.lblTpAmostra = Label(self.container4, text="Tipo Amostra:", font=self.fonte, width=10)
        self.lblTpAmostra.pack(side=LEFT)

        self.txtTpAmostra = Entry(self.container4)
        self.txtTpAmostra["width"] = 25
        self.txtTpAmostra["font"] = self.fonte
        self.txtTpAmostra.pack(side=LEFT)

        self.lbDsObservacoes = Label(self.container5, text="Observações:", font=self.fonte, width=10)
        self.lbDsObservacoes.pack(side=LEFT)

        self.txtDsObservacoes = Entry(self.container5)
        self.txtDsObservacoes["width"] = 25
        self.txtDsObservacoes["font"] = self.fonte
        self.txtDsObservacoes.pack(side=LEFT)

        self.lblIdModelo = Label(self.container6, text="Modelo:", font=self.fonte, width=10)
        self.lblIdModelo.pack(side=LEFT)

        self.txtIdModelo = Entry(self.container6)
        self.txtIdModelo["width"] = 25
        self.txtIdModelo["font"] = self.fonte
        self.txtIdModelo.pack(side=LEFT)

        self.lblIdPessoa = Label(self.container7, text="Pessoa:", font=self.fonte, width=10)
        self.lblIdPessoa.pack(side=LEFT)

        self.txtIdPessoa = Entry(self.container7)
        self.txtIdPessoa["width"] = 25
        self.txtIdPessoa["font"] = self.fonte
        self.txtIdPessoa.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirAmostra
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarAmostra
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirAmostra
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirAmostra(self):
        amostra = Amostra()

        amostra.idAmostra = self.txtIdAmostra.get()
        amostra.dtColetaAmostra = self.txtDtColetaAmostra.get()
        amostra.tpAmostra = self.txtTpAmostra.get()
        amostra.dsObservacoes = self.txtDsObservacoes.get()
        amostra.idModelo = self.txtIdModelo.get()
        amostra.idPessoa = self.txtIdPessoa.get()

        self.lblmsg["text"] = amostra.insert()

        self.txtIdAmostra.delete(0, END)
        self.txtDtColetaAmostra.delete(0, END)
        self.txtTpAmostra.delete(0, END)
        self.txtDsObservacoes.delete(0, END)
        self.txtIdModelo.delete(0, END)
        self.txtIdPessoa.delete(0, END)

    def alterarAmostra(self):

        amostra = Amostra()

        amostra.idAmostra = self.txtIdAmostra.get()
        amostra.dtColetaAmostra = self.txtDtColetaAmostra.get()
        amostra.tpAmostra = self.txtTpAmostra.get()
        amostra.dsObservacoes = self.txtDsObservacoes.get()
        amostra.idModelo = self.txtIdModelo.get()
        amostra.idPessoa = self.txtIdPessoa.get()

        self.lblmsg["text"] = amostra.update()

        self.txtIdAmostra.delete(0, END)
        self.txtDtColetaAmostra.delete(0, END)
        self.txtTpAmostra.delete(0, END)
        self.txtDsObservacoes.delete(0, END)
        self.txtIdModelo.delete(0, END)
        self.txtIdPessoa.delete(0, END)

    def excluirAmostra(self):
        amostra = Amostra()

        amostra.idAmostra = self.txtIdAmostra.get()

        self.lblmsg["text"] = amostra.delete()

        self.txtIdAmostra.delete(0, END)
        self.txtDtColetaAmostra.delete(0, END)
        self.txtTpAmostra.delete(0, END)
        self.txtDsObservacoes.delete(0, END)
        self.txtIdModelo.delete(0, END)
        self.txtIdPessoa.delete(0, END)

    def buscarAmostra(self):
        amostra = Amostra()

        idAmostra = self.txtIdAmostra.get()

        self.lblmsg["text"] = amostra.select(idAmostra)

        self.txtIdAmostra.delete(0, END)
        self.txtIdAmostra.insert(INSERT, amostra.idAmostra)

        self.txtDtColetaAmostra.delete(0, END)
        self.txtDtColetaAmostra.insert(INSERT, amostra.dtColetaAmostra)

        self.txtTpAmostra.delete(0, END)
        self.txtTpAmostra.insert(INSERT, amostra.tpAmostra)

        self.txtDsObservacoes.delete(0, END)
        self.txtDsObservacoes.insert(INSERT, amostra.dsObservacoes)

        self.txtIdModelo.delete(0, END)
        self.txtIdModelo.insert(INSERT, amostra.idModelo)

        self.txtIdPessoa.delete(0, END)
        self.txtIdPessoa.insert(INSERT, amostra.idPessoa)


root = Tk()
Application(root)
root.mainloop()