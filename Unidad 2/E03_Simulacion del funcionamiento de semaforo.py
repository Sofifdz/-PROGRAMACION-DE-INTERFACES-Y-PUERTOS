import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
import numpy as np

qtCreatorFile = "E03_Simulacion del funcionamiento de semaforo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        #self.timer.timeout.connect(self.actualizar_colores)
        self.timer.start(5000)


        self.rojo = QColor(255, 0, 0)
        self.amarillo = QColor(255, 255, 0)
        self.verde = QColor(0, 255, 0)

        self.colors = ["rojo", "amarillo", "verde"]
        self.current_color = self.colors[0]
        self.btnstart.clicked.connect(self.actualizar_colores)
        self.btnDetener.clicked.connect(self.Deneter_colores)

    def actualizar_colores(self):
        try:
            if self.current_color == "verde":
                self.lblrojo.setStyleSheet("background-color: gray")
                self.lblamarillo.setStyleSheet("background-color: gray")
                self.lblverde.setStyleSheet(f"background-color: {self.verde.name()}")
            elif self.current_color == "amarillo":
                self.lblrojo.setStyleSheet("background-color: gray")
                self.lblamarillo.setStyleSheet(f"background-color: {self.amarillo.name()}")
                self.lblverde.setStyleSheet("background-color: gray")
            elif self.current_color == "rojo":
                self.lblrojo.setStyleSheet(f"background-color: {self.rojo.name()}")
                self.lblamarillo.setStyleSheet("background-color: gray")
                self.lblverde.setStyleSheet("background-color: gray")


            self.current_color = self.colors[(self.colors.index(self.current_color) + 1) % len(self.colors)]


        except Exception as error:
            print(error)

    def Deneter_colores(self):
        self.timer.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

