#!/usr/bin/env python
# -*- coding: utf-8 -*-
######################################################################################################################
# This application only returns the selected color from a chooser-dlg to the command line
# It is only constructed for a fast way to determine a colors RGB value
######################################################################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import QTranslator, QLocale, QLibraryInfo
import sys

app = QApplication(sys.argv)
app.setApplicationName("Color Chooser")
qt_translator = QTranslator()
qt_translator.load("qt_" + QLocale.system().name(),
                QLibraryInfo.location(QLibraryInfo.TranslationsPath))
app.installTranslator(qt_translator)

chooserWidget = QColorDialog()
color = chooserWidget.getColor()
if color.isValid():                        #### only if a color was choosen
########################################################### Clipboard
    clipboard = QApplication.clipboard()
    clipboard.setText(color.name())
########################################################## MesageBox
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle("Ihre Codes:")
    msgBox.setText("<b>RGB-Value=</b> {0}, {1}, {2}<br><b>HEX-Code=</b> {3}".format(color.red(), color.green(), color.blue(), color.name()))
    msgBox.setInformativeText("der HEX-Code {0}, wurde bereits in Ihre Zwischenablage kopiert!".format(color.name()))
    msgBox.addButton("Ok", QMessageBox.ActionRole)
    msgBox.exec_()
#print()
#print("".format())

exit()
app.exec_()
