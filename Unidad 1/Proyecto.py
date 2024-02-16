import numpy as np
import statistics
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Proyecto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.btnMayor.clicked.connect(self.Calcmayor)
        self.btnValorMenor.clicked.connect(self.Calcmenor)
        self.btnMedia.clicked.connect(self.Calcmedia)
        self.btnMediana.clicked.connect(self.Calcmediana)
        self.btnModa.clicked.connect(self.Calcmoda)
        self.btnEstandar.clicked.connect(self.desvEstandar)
        self.btnVarianza.clicked.connect(self.Calcvarianza)
        self.txtResultado.setEnabled(False)

        # Área de los Signals
    def Calcmayor(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        mayor = max(lista_en_numeros)
        self.txtResultado.setText(str(mayor))
        pass

    def Calcmenor(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        menor = min(lista_en_numeros)
        self.txtResultado.setText(str(menor))
        pass
    def Calcmedia(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        media = np.mean(lista_en_numeros)
        self.txtResultado.setText(str(media))
        pass
    def Calcmoda(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        moda = statistics.mode(lista_en_numeros)
        self.txtResultado.setText(str(moda))
        pass

    def Calcmediana(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        longitud = len(lista_en_numeros)

        if longitud % 2 == 0:
            # Si la longitud de la lista es par, la mediana es el promedio de los dos valores centrales
            mediana = (lista_en_numeros[longitud // 2 - 1] + lista_en_numeros[longitud // 2]) / 2
        else:
            # Si la longitud de la lista es impar, la mediana es el valor central
            mediana = lista_en_numeros[longitud // 2]

        self.txtResultado.setText(str(mediana))
        pass

    def desvEstandar(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        estandar = statistics.stdev(lista_en_numeros)
        self.txtResultado.setText(str(estandar))
        pass

    def Calcvarianza(self):
        numeros = self.txtNumeros.text()
        lista = numeros.split(" ")
        print(lista)
        lista_en_numeros = [int(i) for i in lista]
        print(lista_en_numeros)

        media = sum(lista_en_numeros) / len(lista_en_numeros)

        sum_cuadrados_diferencias = sum((x - media) ** 2 for x in lista_en_numeros)

        varianza = sum_cuadrados_diferencias / len(lista_en_numeros)
        self.txtResultado.setText(str(varianza))
        pass
    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())