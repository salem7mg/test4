# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_file_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 505)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton_file = QtWidgets.QPushButton(Dialog)
        self.pushButton_file.setGeometry(QtCore.QRect(70, 40, 112, 34))
        self.pushButton_file.setObjectName("pushButton_file")
        self.pushButton_folder = QtWidgets.QPushButton(Dialog)
        self.pushButton_folder.setGeometry(QtCore.QRect(190, 40, 112, 34))
        self.pushButton_folder.setObjectName("pushButton_folder")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Dialog"))
        self.pushButton_file.setText(_translate("Dialog", "Open file"))
        self.pushButton_folder.setText(_translate("Dialog", "Open folder"))

