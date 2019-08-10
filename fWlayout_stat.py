# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fWlayout-stat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stat(object):
    def setupUi(self, Stats):
        Stats.setObjectName("Stats")
        Stats.setGeometry(QtCore.QRect(0, 0, 610, 416))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Stats)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Stats)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.groupBox = QtWidgets.QGroupBox(Stats)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Stats)
        QtCore.QMetaObject.connectSlotsByName(Stats)

    def retranslateUi(self, Stats):
        _translate = QtCore.QCoreApplication.translate
        Stats.setWindowTitle(_translate("Stat", "Stats"))
        self.groupBox.setTitle(_translate("Stat", "Display Control"))
        self.checkBox.setText(_translate("Stat", "Frequency"))
        self.checkBox_5.setText(_translate("Stat", "Cumulative"))
        self.checkBox_4.setText(_translate("Stat", "Show Total"))
        self.pushButton.setText(_translate("Stat", "PushButton"))
