import sys
from PyQt5.QtWidgets import QApplication
from load.load_menu_principal import VentanaMenu
from PyQt5 import QtCore, QtWidgets

if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QtWidgets.QApplication(sys.argv)
    hub_principal = VentanaMenu()
    hub_principal.showMaximized()
    sys.exit(app.exec_())