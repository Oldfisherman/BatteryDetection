# -*- coding: utf-8 -*-

"""
Module implementing LoginDialog.
"""
from PyQt4 import QtGui,QtCore
from PyQt4 import Qt
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QDialog

from Ui_Login import Ui_Login


class Login(QDialog, Ui_Login):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        file = QtCore.QFile('./Qss/Login.qss')
        file.open(QtCore.QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = unicode(styleSheet, encoding='utf-8')
        self.setStyleSheet(styleSheet)
        #make dialog window frameless
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        #make dialog window transparent to realize round edge
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        #set attribute tto delete login dialog
        self.setAttribute(Qt.Qt.WA_DeleteOnClose)

    @pyqtSignature("")
    def on_LoginButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (self.TextUserName.text() == '123' and
                    self.TextPassword.text() == '123'):
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Bad user or password')


    def handleLogin(self):
        if (self.TextUserName.text() == 'foo' and
                    self.TextPassword.text() == 'bar'):
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Bad user or password')
    
    @pyqtSignature("")
    def on_CancelButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #QCoreApplication.quit()
        QCoreApplication.instance().quit()
