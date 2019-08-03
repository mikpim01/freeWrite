#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:35:30 2019

@author: june
"""

import sys
from PyQt5 import QtWidgets, uic

#  QtDesigner imports...
from MainWindow import Ui_MainWindow

# QtDesigner import constructors...
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

# app instance declaration
app = QtWidgets.QApplication(sys.argv)

# mainwindow instance declaration and .show()
window = MainWindow()
window.show()

# Need to open .freeWrite.<userName>.csv
# Need to R/W entry for selected date

# Open the application
app.exec()

# Need to W to .freeWrite.<userName>.csv
