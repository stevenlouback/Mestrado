# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testeHJ.ui'
#



# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 47, 13))
        self.label.setObjectName("label")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(110, 80, 118, 22))
        self.timeEdit.setObjectName("timeEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "TextLabel"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    tela = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(tela)
    tela.show()
    sys.exit(app.exec_())
