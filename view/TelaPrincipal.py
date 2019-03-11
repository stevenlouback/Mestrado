from PyQt5.QtWidgets import QApplication,  QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from FrmAmostra import FrmAmostra
from FrmMatrizX import FrmMatrizX
from FrmAluguel import FrmAluguel
from teste import Example

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


class TelaPrincipal(object):

    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName(_fromUtf8("TelaPrincipal"))
        TelaPrincipal.setWindowModality(QtCore.Qt.NonModal)

        # DESABILITAR REDIMENCIONAMENTO DA JANELA
        TelaPrincipal.setFixedSize(1024, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../imagens/FrmIcon_Car.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipal.setWindowIcon(icon)
        TelaPrincipal.setAutoFillBackground(True)
        #TelaPrincipal.setIconSize(QtCore.QSize(40, 40))

        self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 1024, 101))
        self.columnView.setObjectName(_fromUtf8("columnView"))

        # BTN Amostra #############
        self.btnAmostra = QtWidgets.QPushButton(self.centralwidget)
        self.btnAmostra.setGeometry(QtCore.QRect(10, 10, 131, 81))
        self.btnAmostra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAmostra.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAmostra.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../imagens/chemical-weapon-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAmostra.setIcon(icon1)
        self.btnAmostra.setIconSize(QtCore.QSize(40, 40))
        self.btnAmostra.setObjectName(_fromUtf8("btnAmostra"))
        ##BTN ALUGAR CLICK EVENT ######
        self.btnAmostra.clicked.connect(self.FrmAmostra_Click)

        # BTN Pessoa ###################
        self.btnPessoa = QtWidgets.QPushButton(self.centralwidget)
        self.btnPessoa.setGeometry(QtCore.QRect(140, 10, 131, 81))
        self.btnPessoa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../imagens/user-4-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPessoa.setIcon(icon2)
        self.btnPessoa.setIconSize(QtCore.QSize(30, 30))
        self.btnPessoa.setObjectName(_fromUtf8("btnPessoa"))
        ##  BTNCLIENTE CLICK EVENT  ###
        self.btnPessoa.clicked.connect(self.FrmPessoa_Click)

        # BTN MatrizX ###################
        self.btnMatrizX = QtWidgets.QPushButton(self.centralwidget)
        self.btnMatrizX.setGeometry(QtCore.QRect(270, 10, 131, 81))
        self.btnMatrizX.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../imagens/data-configuration-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMatrizX.setIcon(icon3)
        self.btnMatrizX.setIconSize(QtCore.QSize(30, 30))
        self.btnMatrizX.setObjectName(_fromUtf8("btnMatrizX"))
        ##  BTNCLIENTE CLICK EVENT  ###
        self.btnMatrizX.clicked.connect(self.FrmMatrizX_Click)

        self.lbImg = QtWidgets.QLabel(self.centralwidget)
        self.lbImg.setGeometry(QtCore.QRect(7, 110, 1010, 570))
        self.lbImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbImg.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbImg.setText(_fromUtf8(""))
        self.lbImg.setPixmap(QtGui.QPixmap(_fromUtf8("../imagens/Química-macetes.png")))
        #self.lbImg.setAlignment(Qt.QTabletEvent.AlignJustify | Qt.AlignVCenter)
        self.lbImg.setObjectName(_fromUtf8("lbImg"))
        #TelaPrincipal.setCentralWidget(self.centralwidget)

        self.actionAmostra = QtWidgets.QAction(TelaPrincipal)
        self.actionAmostra.setObjectName(_fromUtf8("actionAmostra"))

        self.actionPessoa = QtWidgets.QAction(TelaPrincipal)
        self.actionPessoa.setObjectName(_fromUtf8("actionPessoa"))

        self.actionMatrizX = QtWidgets.QAction(TelaPrincipal)
        self.actionMatrizX.setObjectName(_fromUtf8("actionMatrizX"))

        self.retranslateUi(TelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        TelaPrincipal.setWindowTitle(_translate("Tela Principal", "Sistema de Análises do PH", None))

        self.btnAmostra.setText(_translate("TelaPrincipal", "Amostras", None))
        self.btnPessoa.setText(_translate("TelaPrincipal", "Pessoas", None))
        self.btnMatrizX.setText(_translate("TelaPrincipal", "Matriz X", None))

        self.actionAmostra.setText(_translate("TelaPrincipal", "Amostra", None))
        self.actionPessoa.setText(_translate("TelaPrincipal", "Pessoas", None))
        self.actionMatrizX.setText(_translate("TelaPrincipal", "MatrizX", None))

    # BTN AMOSTRA.CLICK
    def FrmAmostra_Click(self):
        self.frmAmostra = QMainWindow()
        self.ui = FrmAmostra()
        self.ui.setupUi(self.frmAmostra)
        self.frmAmostra.show()

    # BTNPESSOA.CLICK
    def FrmPessoa_Click(self):
        self.frmPessoa = QMainWindow()
        self.ui = Example()
        self.ui.setupUi(self.frmPessoa)
        self.frmPessoa.show()

    # BTNMATRIZX.CLICK
    def FrmMatrizX_Click(self):
        self.frmMatrizX = QMainWindow()
        self.ui = FrmMatrizX()
        self.ui.setupUi(self.frmMatrizX)
        self.frmMatrizX.show()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    tela = QtWidgets.QWidget()
    ui = TelaPrincipal()
    ui.setupUi(tela)
    tela.show()
    sys.exit(app.exec_())


