#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""

freeWrite 

An application for the collection and archival of personal logs. The application should encourage daily logging and review. The application should discourage deletion or revision.

author contact: raydialow@raydialow.xyz

"""
import sys
from PyQt5 import QtWidgets
from fWapp import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
