from PyQt5.QtWidgets import QApplication,  QMainWindow, QMessageBox, QAbstractItemView
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

import sys

sys.path.append("..\dao")
sys.path.append("..\metodos")

from DAOmatrizy import Matrizy
from DAOmatrizx import Matrizx
from pls import PLS1
from pca import PCA
from tkinter import *

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

class FrmMatrizX(object):
    def setupUi(self, MatrizX):
        MatrizX.setObjectName("MatrizX")
        MatrizX.resize(574, 576)
        self.groupBox = QtWidgets.QGroupBox(MatrizX)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 551, 221))
        self.groupBox.setObjectName("groupBox")

        self.txtIdModelo = QtWidgets.QLineEdit(self.groupBox)
        self.txtIdModelo.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.txtIdModelo.setObjectName("txtIdModelo")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")

        self.btnBuscar = QtWidgets.QPushButton(self.groupBox)
        self.btnBuscar.setGeometry(QtCore.QRect(430, 40, 75, 23))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnBuscar.clicked.connect(lambda: self.buscarAmostraModelo())

        self.lblmsg = QtWidgets.QLabel(self.groupBox)
        self.lblmsg.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.lblmsg.setObjectName("lblmsg")

        self.retranslateUi(MatrizX)
        QtCore.QMetaObject.connectSlotsByName(MatrizX)

    def retranslateUi(self, Amostras):
        _translate = QtCore.QCoreApplication.translate
        Amostras.setWindowTitle(_translate("MatrizX", "Matriz X"))
        self.groupBox.setTitle(_translate("MatrizX", "MatrizX"))
        self.label.setText(_translate("MatrizX", "Nº Modelo"))
        self.btnBuscar.setText(_translate("Amostras", "Buscar"))
        self.lblmsg.setText(_translate("Amostras", "TextLabel"))

    def buscarAmostraModelo(self):
        matrizX = Matrizx()

        matrizY = Matrizy()

        idModelo = self.txtIdModelo.text()

        YY = matrizY.selectMatrizyYNOVO(idModelo)

        XX = matrizX.selectMatrizXModeloNOVO(idModelo)

        pls_1 = PLS1(X=XX, Y=YY, g=1, epsilon=DEFAULT_EPSILON, ignore_failures=False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    tela = QtWidgets.QDialog()
    ui = FrmMatrizX()
    ui.setupUi(tela)
    tela.show()
   # sys.exit(app.exec_())