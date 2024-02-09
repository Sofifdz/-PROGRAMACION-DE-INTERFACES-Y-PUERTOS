import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmeticas_conEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnSumar.clicked.connect(self.operacion)
        self.btnResta.clicked.connect(self.operacion)
        self.btnMultiplicar.clicked.connect(self.operacion)
        self.btnDivision.clicked.connect(self.operacion)

        self.txtResultado.setEnabled(False) #deshabilita el cuadro de texto


    def operacion(self):
        try:
            objeto = self.sender()
            nombre = objeto.objectName()
            print(nombre)

            A= int(self.txtA.text())
            B =int(self.txtB.text())

            if nombre == "btnSumar":
                r= A+B
            elif nombre == "btnResta":
                r= A-B
            elif nombre == "btnMultiplicar":
                r= A*B
            elif nombre == "btnDivision":
                r= A/B
            self.txtResultado.setText(str(r))
        except Exception as error:
            print(error)
        pass




        # Área de los Signals

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

