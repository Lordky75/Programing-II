from PyQt5 import QtWidgets, uic
from ejercicio2.psp2 import integracionSimpson

class VentanaPSP2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_2.ui", self)
        self.btnCalcular.clicked.connect(self.btnCalcularClick)
        self.btnCaso1.clicked.connect(self.btnCaso1Click)
        self.btnCaso2.clicked.connect(self.btnCaso2Click)
        self.btnCaso3.clicked.connect(self.btnCaso3Click)
        self.btnCaso4.clicked.connect(self.btnCaso4Click)
        self.btnSalir.clicked.connect(self.close)

    def btnCalcularClick(self):
        try:
            val_x = float(self.editX.text())
            val_dof = float(self.editDof.text())
            cal = integracionSimpson(val_x, val_dof)
            cal.calcularOperaciones()
            self.labelPResultado.setText(f"{cal.p:.5f}")
                
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error")

    def btnCaso1Click(self):
        self.editX.setText("1.1")
        self.editDof.setText("9")
        
    def btnCaso2Click(self):
        self.editX.setText("1.1812")
        self.editDof.setText("10")
        
    def btnCaso3Click(self):
        self.editX.setText("2.750")
        self.editDof.setText("30")
    
    def btnCaso4Click(self):
        self.editX.setText("1.846")
        self.editDof.setText("14")