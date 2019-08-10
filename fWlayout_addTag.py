# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fWlayout-addTag.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTag(object):
    def setupUi(self, AddTag):
        AddTag.setObjectName("AddTag")
        AddTag.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(AddTag)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(AddTag)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(AddTag)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddTag)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        self.textBrowser = QtWidgets.QTextBrowser(AddTag)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.lineEdit = QtWidgets.QLineEdit(AddTag)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.retranslateUi(AddTag)
        self.buttonBox.accepted.connect(AddTag.Dialog.accept)
        self.buttonBox.rejected.connect(AddTag.Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTag)

    def retranslateUi(self, AddTag):
        _translate = QtCore.QCoreApplication.translate
        AddTag.setWindowTitle(_translate("AddTag", "Add Tag"))
        self.label_2.setText(_translate("AddTag", "Selected Entrys"))
        self.label.setText(_translate("AddTag", "Additional Tag"))
