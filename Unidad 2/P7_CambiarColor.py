import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P7_CanbiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        # Área de los Signals
        self.txtR_2.setMinimum(0)
        self.txtR_2.setMaximum(255)
        self.txtR_2.setSingleStep(1)
        self.txtR_2.setValue(0)
        self.txtR_2.valueChanged.connect(self.cambiaR)

        self.txtG_2.setMinimum(0)
        self.txtG_2.setMaximum(255)
        self.txtG_2.setSingleStep(1)
        self.txtG_2.setValue(0)
        self.txtG_2.valueChanged.connect(self.cambiaG)

        self.txtB_2.setMinimum(0)
        self.txtB_2.setMaximum(255)
        self.txtB_2.setSingleStep(1)
        self.txtB_2.setValue(0)
        self.txtB_2.valueChanged.connect(self.cambiaB)

        # Do not overwrite QLineEdit objects with integer values
        self.initial_txtR_2 = 0
        self.initial_txtG_2 = 0
        self.initial_txtB_2 = 0

    # Área de los Slots

    def cambiaR(self):
        try:
            self.initial_txtR_2 = self.txtR_2.value()
            estilo = ("background-color: rgb(" + str(self.initial_txtR_2) +
                      "," + str(self.initial_txtG_2) + "," + str(self.initial_txtB_2) + ");")
            self.colores.setStyleSheet(estilo)

        except Exception as error:
            print(error)

    def cambiaG(self):
        try:
            self.initial_txtG_2 = self.txtG_2.value()
            estilo = ("background-color: rgb(" + str(self.initial_txtR_2) +
                      "," + str(self.initial_txtG_2) + "," + str(self.initial_txtB_2) + ");")
            self.colores.setStyleSheet(estilo)
        except Exception as error:
            print(error)

    def cambiaB(self):
        try:
            self.initial_txtB_2 = self.txtB_2.value()
            estilo = ("background-color: rgb(" + str(self.initial_txtR_2) +
                      "," + str(self.initial_txtG_2) + "," + str(self.initial_txtB_2) + ");")
            self.colores.setStyleSheet(estilo)
        except Exception as error:
            print(error)

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

