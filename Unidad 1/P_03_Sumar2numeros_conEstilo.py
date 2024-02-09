import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_Sumar2numeros_conEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnSumar.clicked.connect(self.sumar)
        self.txtSuma.setEnabled(False) #deshabilita el cuadro de texto


    def sumar(self):
        A= int(self.txtA.text())
        B =int(self.txtB.text())
        r= A+B
        self.txtSuma.setText(str(r))
        pass

        # Área de los Signals

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

