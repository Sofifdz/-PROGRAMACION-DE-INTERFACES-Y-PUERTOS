import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmeticas_conEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnSumar.clicked.connect(self.sumar)
        self.btnResta.clicked.connect(self.restar)
        self.btnMultiplicar.clicked.connect(self.multiplicar)
        self.btnDivision.clicked.connect(self.dividir)
        self.txtResultado.setEnabled(False) #deshabilita el cuadro de texto


    def sumar(self):
        A= int(self.txtA.text())
        B =int(self.txtB.text())
        r= A+B
        self.txtResultado.setText(str(r))
        pass
    def restar(self):
        A = int(self.txtA.text())
        B = int(self.txtB.text())
        rr = A - B
        self.txtResultado.setText(str(rr))
        pass
    def multiplicar(self):
        A = int(self.txtA.text())
        B = int(self.txtB.text())
        rm = A * B
        self.txtResultado.setText(str(rm))
        pass

    def dividir(self):
        A = int(self.txtA.text())
        B = int(self.txtB.text())
        rd = A / B
        self.txtResultado.setText(str(rd))
        pass


        # Área de los Signals

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

