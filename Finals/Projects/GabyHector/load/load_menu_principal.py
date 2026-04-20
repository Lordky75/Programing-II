import os
from PyQt5 import QtWidgets, uic
from load.load_venta_psp1 import VentanaPSP1 
from load.load_venta_psp2 import VentanaPSP2
from PyQt5 import QtCore 

class VentanaMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gui", "menu.ui"))
        uic.loadUi("gui/ventana_menu.ui", self)
        self.showMaximized()
        self.ActionPSP1.triggered.connect(self.abrir_psp1)
        self.ActionPSP2.triggered.connect(self.abrir_psp2)
        
    def abrir_psp1(self):
        vp1 = VentanaPSP1()
        vp1.exec()

    def abrir_psp2(self):
        vp2 = VentanaPSP2()
        vp2.exec()