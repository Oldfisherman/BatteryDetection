from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_MainWindow import Ui_MainWindow
from MainWindow import MainWindow
from Login import Login
import PictureResource_rc

import sys, time
from time import time, sleep
import ctypes

from tendo import singleton

def main ():

    #make sure to shown tacskIcon right when use pyinstaller to make exe file you can commont it
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("BatterayDetection")

    me = singleton.SingleInstance()
    app = QtGui.QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(":/Start/Resource/start.png"), Qt.WindowStaysOnTopHint)
    splash.setDisabled(True)  # Disables widget input events, or when mouse click splash will be hide
    splash.show()
    splash.showMessage("Start Application ......", Qt.AlignBottom, Qt.black)
    app.processEvents()

    start = time()
    while time() - start < 1:
        sleep(0.1)
        app.processEvents()

    login = Login()
    #login.show()
    splash.finish(login)

    if (login.exec_() == QtGui.QDialog.Accepted) :
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
   main()


