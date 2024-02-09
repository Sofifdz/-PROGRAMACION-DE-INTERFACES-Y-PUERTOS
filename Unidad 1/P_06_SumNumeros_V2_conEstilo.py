import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_SumNumeros_V2_conEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnSumar.clicked.connect(self.sumar)
        self.txtResultado.setEnabled(False) #deshabilita el cuadro de texto


    def sumar(self):

        #usuario ingresara los numeros separados por espacios
        numeros = self.txtNumeros.text()#entrada ejmemplo: 5 7 8 9
        lista = numeros.split(" ") #convierte la entra de numeros en una lista Ejemplo: ['1','2','3','4','5',' 7',' 8', '9']
        print(lista)
        lista_en_numeros = [int(i) for i in lista] #convsersion de los caracteres a numeros
        print(lista_en_numeros)

        suma = sum(lista_en_numeros)
        self.txtResultado.setText(str(suma))
        pass

        # Área de los Signals

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

