import sys
import random

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer

qtCreatorFile = "E_01_JuegoDeMemoria.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.colores = ['red', 'green', 'blue', 'yellow']
        self.patron = []
        self.patron_ingresado = []

        self.rojo.clicked.connect(self.seleccion)
        self.verde.clicked.connect(self.seleccion)
        self.azul.clicked.connect(self.seleccion)
        self.amarillo.clicked.connect(self.seleccion)

        self.btnComenzar.clicked.connect(self.comenzar_juego)
        self.btnVerificar.clicked.connect(self.verificar_patron)

        self.rojo.setStyleSheet(f'background-color: gray')
        self.verde.setStyleSheet(f'background-color: gray')
        self.azul.setStyleSheet(f'background-color: gray')
        self.amarillo.setStyleSheet(f'background-color: gray')


        self.color_index = 0

    def seleccion(self):
        pass



    def comenzar_juego(self):
        try:
            t = self.btnComenzar.text()
            if t == "Iniciar":
                self.btnComenzar.setText("DETENER")
                #aqui se crea una lista patron que contiene 5 numeros leatorios entre 0 y la long de colores -1
                self.patron = [random.randint(0, len(self.colores) - 1) for _ in range(5)]
                self.patron_ingresado = []
                self.mostrar_patron()
            else:
                self.btnComenzar.setText("Iniciar")
                self.timer.stop()
        except Exception as error:
            print(error)



    def mostrar_patron(self):
        try:

            self.btnVerificar.setEnabled(False)
            self.timer = QTimer(self)#aqui me crea un temporizador
            self.timer.timeout.connect(self.ocultar_patron)#se configura el temporizador por ocultar patron para cuando este termine el patron se oculte
            self.color_index = 0
            self.mostrar_siguiente_color()
        except Exception as error:
            print(error)

    def mostrar_siguiente_color(self):
        if self.color_index < len(self.patron):#si aun no se termina de mostrar los colores ocurre:
            index = self.patron[self.color_index]#aqui se obtiene el indice del color actual del patron y abajo se incrementa para el sig color
            self.color_index += 1
            color = self.colores[index]
            getattr(self, f'{color}').setStyleSheet(f'background-color: {color}')#se configura el estilo para mpstrar el color del patron
            self.timer.start(1000)#inicia un temporizador para ocultar el color despues de un segundo
            self.patron_ingresado.append(self.color_index)#agrega el indice de color a patron ingresado
        else:
            #si ya se termino de mostrar los colores el tempporizador se detiene
            self.timer.stop()
            self.btnVerificar.setEnabled(True)

    def ocultar_patron(self):
        '''este metodo borra los colores de los botones'''
        try:
            for color in self.colores:
                getattr(self, f'btnColor_{color}').setStyleSheet('')
            self.timer.stop()
            QTimer.singleShot(600, self.mostrar_siguiente_color)#despues de 600 milisegundos manda a llamar al metodo de mostrar siguiente color
        except Exception as error:
            print(error)

    def reiniciar_juego(self):
        self.patron = []
        self.patron_ingresado = []
        self.btnComenzar.setEnabled(True)
        self.btnVerificar.setEnabled(False)
        print("Presiona 'Comenzar' para jugar de nuevo.")

    def verificar_patron(self):
        print(self.patron)
        print(self.patron_ingresado)
        if len(self.patron_ingresado) == len(self.patron):
            for i in range(len(self.patron)):
                if self.patron_ingresado[i] != self.patron[i]:
                    print("¡Patrón incorrecto!")
                    self.reiniciar_juego()
                    return
            print("¡Patrón correcto!")
            self.reiniciar_juego()
        else:
            print("¡Patrón incorrecto!")
            self.reiniciar_juego()

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

