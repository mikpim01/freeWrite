# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fWlayout-viewTag.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewTag(object):
    def setupUi(self, ViewTag):
        ViewTag.setObjectName("ViewTag")
        ViewTag.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(ViewTag)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ViewTag)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(ViewTag)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(ViewTag)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.textBrowser = QtWidgets.QTextBrowser(ViewTag)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewTag)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(ViewTag)
        self.buttonBox.accepted.connect(ViewTag.Dialog.accept)
        self.buttonBox.rejected.connect(ViewTag.Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewTag)

    def retranslateUi(self, ViewTag):
        _translate = QtCore.QCoreApplication.translate
        ViewTag.setWindowTitle(_translate("ViewTag", "View Tag"))
        self.label.setText(_translate("ViewTag", "Tag(s)"))
        self.label_2.setText(_translate("ViewTag", "Result(s)"))
