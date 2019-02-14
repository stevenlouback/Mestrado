from PyQt5.QtWidgets import QApplication,  QMainWindow, QMessageBox, QAbstractItemView
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

import sys

sys.path.append("..\dao")

from DAOamostra import Amostra


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class FrmAmostra(object):
    def setupUi(self, Amostras):
        Amostras.setObjectName("Amostras")
        Amostras.resize(574, 576)
        self.groupBox = QtWidgets.QGroupBox(Amostras)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 551, 221))
        self.groupBox.setObjectName("groupBox")
        self.txtIdAmostra = QtWidgets.QLineEdit(self.groupBox)
        self.txtIdAmostra.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.txtIdAmostra.setObjectName("txtIdAmostra")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.txtDtColetaAmostra = QtWidgets.QDateEdit(self.groupBox)
        self.txtDtColetaAmostra.setGeometry(QtCore.QRect(100, 40, 110, 22))
        self.txtDtColetaAmostra.setObjectName("txtDtColetaAmostra")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txtTpAmostra = QtWidgets.QLineEdit(self.groupBox)
        self.txtTpAmostra.setGeometry(QtCore.QRect(220, 40, 61, 20))
        self.txtTpAmostra.setObjectName("txtTpAmostra")
        self.txtIdModelo = QtWidgets.QLineEdit(self.groupBox)
        self.txtIdModelo.setGeometry(QtCore.QRect(290, 40, 61, 20))
        self.txtIdModelo.setObjectName("txtIdModelo")
        self.txtIdPessoa = QtWidgets.QLineEdit(self.groupBox)
        self.txtIdPessoa.setGeometry(QtCore.QRect(360, 40, 61, 20))
        self.txtIdPessoa.setObjectName("txtIdPessoa")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(290, 20, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 20, 51, 16))
        self.label_5.setObjectName("label_5")
        self.txtDsObservacoes = QtWidgets.QTextEdit(self.groupBox)
        self.txtDsObservacoes.setGeometry(QtCore.QRect(20, 80, 511, 41))
        self.txtDsObservacoes.setObjectName("txtDsObservacoes")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_6.setObjectName("label_6")

        self.bntInsert = QtWidgets.QPushButton(self.groupBox)
        self.bntInsert.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.bntInsert.setObjectName("bntInsert")

        self.bntAlterar = QtWidgets.QPushButton(self.groupBox)
        self.bntAlterar.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.bntAlterar.setObjectName("bntAlterar")

        self.bntExcluir = QtWidgets.QPushButton(self.groupBox)
        self.bntExcluir.setGeometry(QtCore.QRect(200, 140, 75, 23))
        self.bntExcluir.setObjectName("bntExcluir")

        self.btnBuscar = QtWidgets.QPushButton(self.groupBox)
        self.btnBuscar.setGeometry(QtCore.QRect(430, 40, 75, 23))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnBuscar.clicked.connect(lambda: self.buscarAmostra())

        self.lblmsg = QtWidgets.QLabel(self.groupBox)
        self.lblmsg.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.lblmsg.setObjectName("lblmsg")

        self.retranslateUi(Amostras)
        QtCore.QMetaObject.connectSlotsByName(Amostras)

    def retranslateUi(self, Amostras):
        _translate = QtCore.QCoreApplication.translate
        Amostras.setWindowTitle(_translate("Amostras", "Controle de Amostras"))
        self.groupBox.setTitle(_translate("Amostras", "Amostra"))
        self.label.setText(_translate("Amostras", "Nº Amostra"))
        self.label_2.setText(_translate("Amostras", "Data Coleta"))
        self.label_3.setText(_translate("Amostras", "Tipo"))
        self.label_4.setText(_translate("Amostras", "Modelo"))
        self.label_5.setText(_translate("Amostras", "Pessoa"))
        self.label_6.setText(_translate("Amostras", "Observações"))
        self.bntInsert.setText(_translate("Amostras", "Insert"))
        self.bntAlterar.setText(_translate("Amostras", "Alterar"))
        self.bntExcluir.setText(_translate("Amostras", "Excluir"))
        self.btnBuscar.setText(_translate("Amostras", "Buscar"))
        self.lblmsg.setText(_translate("Amostras", "TextLabel"))

    def inserirAmostra(self):
        '''amostra = Amostra()

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
        self.txtIdPessoa.delete(0, END)'''

    def alterarAmostra(self):

        '''amostra = Amostra()

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
        self.txtIdPessoa.delete(0, END)'''

    def excluirAmostra(self):
        '''amostra = Amostra()

        amostra.idAmostra = self.txtIdAmostra.get()

        self.lblmsg["text"] = amostra.delete()

        self.txtIdAmostra.delete(0, END)
        self.txtDtColetaAmostra.delete(0, END)
        self.txtTpAmostra.delete(0, END)
        self.txtDsObservacoes.delete(0, END)
        self.txtIdModelo.delete(0, END)
        self.txtIdPessoa.delete(0, END)'''

    def buscarAmostra(self):
        amostra = Amostra()

        idAmostra = self.txtIdAmostra.text()

        self.lblmsg.setText(amostra.select(idAmostra))

        self.txtIdAmostra.setText('')
        self.txtIdAmostra.setText(str(amostra.idAmostra))

        self.txtDtColetaAmostra.setText('')
        #self.txtDtColetaAmostra.setDate(strptime())

        self.txtTpAmostra.setText('')
        self.txtTpAmostra.setText(amostra.tpAmostra)

        self.txtDsObservacoes.setText('')
        self.txtDsObservacoes.setText(amostra.dsObservacoes)

        self.txtIdModelo.setText('')
        self.txtIdModelo.setText(str(amostra.idModelo))

        self.txtIdPessoa.setText('')
        self.txtIdPessoa.setText(str(amostra.idPessoa))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    tela = QtWidgets.QDialog()
    ui = FrmAmostra()
    ui.setupUi(tela)
    tela.show()
    sys.exit(app.exec_())