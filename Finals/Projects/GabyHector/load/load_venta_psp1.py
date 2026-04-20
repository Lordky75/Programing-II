from PyQt5 import QtWidgets, uic
from ejercicio1.psp1 import calculadoraRegresion

class VentanaPSP1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_1.ui", self)
        self.btnMas.clicked.connect(self.btnMasClick)
        self.btnMenos.clicked.connect(self.btnMenosClick)
        self.btnCalcular.clicked.connect(self.btnCalcularClick)
        self.btnCaso1.clicked.connect(self.btnCaso1Click)
        self.btnCaso2.clicked.connect(self.btnCaso2Click)
        self.btnCaso3.clicked.connect(self.btnCaso3Click)
        self.btnCaso4.clicked.connect(self.btnCaso4Click)
        self.btnSalir.clicked.connect(self.close)

    def btnMasClick(self):
        filasActuales = self.tablaDatos.rowCount()
        self.tablaDatos.insertRow(filasActuales)

    def btnMenosClick(self):
        filasActuales = self.tablaDatos.rowCount()
        if filasActuales > 0:
            self.tablaDatos.removeRow(filasActuales - 1)

    def btnCalcularClick(self):
        datosX = []
        datosY = []
        
        try:
            filas = self.tablaDatos.rowCount()
            for i in range(filas):
                item_x = self.tablaDatos.item(i, 0)
                item_y = self.tablaDatos.item(i, 1)
                
                if item_x is not None and item_y is not None:
                    datosX.append(float(item_x.text()))
                    datosY.append(float(item_y.text()))
            
            xk_val = float(self.editXk.text())
            cal = calculadoraRegresion(datosX, datosY, xk_val)
            cal.calcularOperaciones()
            self.labelB0Resultado.setText(f"{cal.beta0:.4f}")
            self.labelB1Resultado.setText(f"{cal.beta1:.4f}")
            self.labelRResultado.setText(f"{cal.r:.4f}")
            self.labelR2Resultado.setText(f"{cal.r2:.4f}")
            self.labelYkResultado.setText(f"{cal.yk:.4f}")
               
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error")

    def btnCaso1Click(self):
        x_test = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        y_test = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        self.llenar_tabla(x_test, y_test)
    
    def btnCaso2Click(self):
        x_test = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        y_test = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
        self.llenar_tabla(x_test, y_test)

    def btnCaso3Click(self):
        x_test = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
        y_test = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        self.llenar_tabla(x_test, y_test)

    def btnCaso4Click(self):
        x_test = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
        y_test = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
        self.llenar_tabla(x_test, y_test)
        
    def llenar_tabla(self, x_test, y_test):
        self.tablaDatos.setRowCount(0)
        for i in range(len(x_test)):
            self.btnMasClick()
            self.tablaDatos.setItem(i, 0, QtWidgets.QTableWidgetItem(str(x_test[i])))
            self.tablaDatos.setItem(i, 1, QtWidgets.QTableWidgetItem(str(y_test[i])))
        self.editXk.setText("386")