# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(401, 311)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(20, 20))
        Login.setBaseSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Start/Resource/Graphicloads-100-Flat-2-Battery-full.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(_fromUtf8(""))
        self.LoginFrame = QtGui.QFrame(Login)
        self.LoginFrame.setGeometry(QtCore.QRect(0, 0, 401, 311))
        self.LoginFrame.setStyleSheet(_fromUtf8(""))
        self.LoginFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.LoginFrame.setObjectName(_fromUtf8("LoginFrame"))
        self.DefondGraphicsView = QtGui.QGraphicsView(self.LoginFrame)
        self.DefondGraphicsView.setGeometry(QtCore.QRect(50, 20, 300, 93))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DefondGraphicsView.sizePolicy().hasHeightForWidth())
        self.DefondGraphicsView.setSizePolicy(sizePolicy)
        self.DefondGraphicsView.setStyleSheet(_fromUtf8("border-image: url(:/Start/Resource/defond_w300.png);"))
        self.DefondGraphicsView.setObjectName(_fromUtf8("DefondGraphicsView"))
        self.LoginButton = QtGui.QPushButton(self.LoginFrame)
        self.LoginButton.setGeometry(QtCore.QRect(50, 260, 121, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginButton.sizePolicy().hasHeightForWidth())
        self.LoginButton.setSizePolicy(sizePolicy)
        self.LoginButton.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.LoginButton.setFont(font)
        self.LoginButton.setCheckable(False)
        self.LoginButton.setObjectName(_fromUtf8("LoginButton"))
        self.QHorizontalLayoutPassword = QtGui.QWidget(self.LoginFrame)
        self.QHorizontalLayoutPassword.setGeometry(QtCore.QRect(50, 190, 301, 51))
        self.QHorizontalLayoutPassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QHorizontalLayoutPassword.setObjectName(_fromUtf8("QHorizontalLayoutPassword"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.QHorizontalLayoutPassword)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.QHorizontalLayoutPassword)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(20, 20))
        self.graphicsView_2.setBaseSize(QtCore.QSize(20, 20))
        self.graphicsView_2.setStyleSheet(_fromUtf8("border-image: url(:/Start/Resource/login_password.png);\n"
"background-color: rgb(255, 255, 255);"))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.horizontalLayout_2.addWidget(self.graphicsView_2)
        self.TextPassword = QtGui.QLineEdit(self.QHorizontalLayoutPassword)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextPassword.sizePolicy().hasHeightForWidth())
        self.TextPassword.setSizePolicy(sizePolicy)
        self.TextPassword.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.TextPassword.setFont(font)
        self.TextPassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-width:0;border-style:outset;"))
        self.TextPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.TextPassword.setObjectName(_fromUtf8("TextPassword"))
        self.horizontalLayout_2.addWidget(self.TextPassword)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.QHorizontalLayoutUserName = QtGui.QWidget(self.LoginFrame)
        self.QHorizontalLayoutUserName.setGeometry(QtCore.QRect(50, 130, 301, 51))
        self.QHorizontalLayoutUserName.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QHorizontalLayoutUserName.setObjectName(_fromUtf8("QHorizontalLayoutUserName"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.QHorizontalLayoutUserName)
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.QHorizontalLayoutUserName)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(20, 20))
        self.graphicsView.setBaseSize(QtCore.QSize(20, 20))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/Start/Resource/login_user.png);\n"
"background-color: rgb(255, 255, 255);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.TextUserName = QtGui.QLineEdit(self.QHorizontalLayoutUserName)
        self.TextUserName.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextUserName.sizePolicy().hasHeightForWidth())
        self.TextUserName.setSizePolicy(sizePolicy)
        self.TextUserName.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        self.TextUserName.setFont(font)
        self.TextUserName.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-width:0;border-style:outset;"))
        self.TextUserName.setObjectName(_fromUtf8("TextUserName"))
        self.horizontalLayout.addWidget(self.TextUserName)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.CancelButton = QtGui.QPushButton(self.LoginFrame)
        self.CancelButton.setGeometry(QtCore.QRect(220, 260, 128, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.CancelButton.setFont(font)
        self.CancelButton.setAutoDefault(False)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.LoginButton.setText(_translate("Login", "Login", None))
        self.TextPassword.setPlaceholderText(_translate("Login", "Password", None))
        self.TextUserName.setWhatsThis(_translate("Login", "<html><head/><body><p><br/></p></body></html>", None))
        self.TextUserName.setPlaceholderText(_translate("Login", "UserName", None))
        self.CancelButton.setText(_translate("Login", "Cancel", None))

import PictureResource_rc
