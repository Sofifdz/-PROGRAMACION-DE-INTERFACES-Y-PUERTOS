import serial
import sys
from PyQt5 import uic, QtGui, QtWidgets, QtCore

qtCreatorFile = "Leds.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnConectar.clicked.connect(self.conexion)
        self.temporizador = QtCore.QTimer()
        self.temporizador.timeout.connect(self.leerDatosArduino)
        self.temporizador.setInterval(1000)
        self.estadoConexion = -1
        self.dispositivoArduino = None

    def leerDatosArduino(self):
        if self.dispositivoArduino is not None and self.dispositivoArduino.isOpen():
            datos = self.dispositivoArduino.readline().decode().strip()
            if datos != "":
                self.lbl_leds.setText(datos)

    def conexion(self):
        if self.estadoConexion == -1:
            self.dispositivoArduino = serial.Serial(port='com4', baudrate=9600, timeout=10)
            self.btnConectar.setText("Desconectar")
            self.estadoConexion = 1
            self.temporizador.start()
        elif self.estadoConexion == 0:
            self.dispositivoArduino.open()
            self.btnConectar.setText("Desconectar")
            self.estadoConexion = 1
            self.temporizador.start()
        elif self.estadoConexion == 1:
            self.dispositivoArduino.close()
            self.btnConectar.setText("Conectar")
            self.estadoConexion = 0
            self.temporizador.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MyApp()
    ventana.show()
    sys.exit(app.exec_())
