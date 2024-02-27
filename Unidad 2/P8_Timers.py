import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P8_Timers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#ACTUALIZAR IMAGENES :pyrcc5 recursos.qrc -o recursos_rc.py

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_iniciar2.clicked.connect(self.iniciar2)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.contar)

    def iniciar(self):
        try:
            import time as t
            text = self.txtNumero.toPlainText().strip()
            if text:
                n = int(text)
                print(n)
                for i in range(n):
                    self.txtContador.setText(str(i + 1))
                    t.sleep(0.5)
                    print(i + 1)
        except ValueError as error:
            print("Error converting to integer:", error)
        except Exception as error:
            print(error)

    def iniciar2(self):
        try:
            text_2 = self.txtNumero_2.toPlainText().strip()
            if text_2:
                self.num = int(text_2)
                print(self.num)
                self.segundoPlano.start(500)
                self.cont = 1
                self.txtContador_2.setText("1")
        except ValueError as error:
            print("Error converting to integer:", error)
        except Exception as error:
            print(error)

    def contar(self):
        try:
            if self.cont < self.num:
                self.cont += 1
                self.txtContador_2.setText(str(self.cont))
            else:
                self.segundoPlano.stop()
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

