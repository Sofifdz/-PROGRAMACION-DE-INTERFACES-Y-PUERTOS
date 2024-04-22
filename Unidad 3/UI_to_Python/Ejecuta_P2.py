from UI_to_Python import P2_Ejemplo as interfaz
import sys
from PyQt5 import uic, QtWidgets
#qtCreatorFile = "P1_Ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_saludomundo.clicked.connect(self.saludo)


    # Área de los Slots
    def saludo(self):
       try:
           self.nombre.setText("Hola mundo")
           self.btn_saludomundo.hide()
       except Exception as e:
           print(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

