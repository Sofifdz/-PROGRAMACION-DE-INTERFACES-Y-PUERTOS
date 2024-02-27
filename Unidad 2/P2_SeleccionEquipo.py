import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#ACTUALIZAR IMAGENES :pyrcc5 recursos.qrc -o recursos_rc.py

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cbUriel.toggled.connect(self.selfUriel)
        self.cbEduardo.toggled.connect(self.selfEduardo)
        self.cbBadillo.toggled.connect(self.selfBadillo)
        self.cbSofi.toggled.connect(self.selfSofi)

        self.uriel = " "
        self.eduardo = " "
        self.badillo = " "
        self.sofi = " "

    def selfUriel(self):
        try:
            if self.cbUriel.isChecked():
                print("Uriel true")
                self.uriel = "Uriel\n"

            else:
                print("Uriel false")
                self.uriel = " "
            self.txtEquipo.setPlainText(self.uriel +self.badillo+self.eduardo+self.sofi)
        except Exception as error:
            print(error)
    def selfEduardo(self):
        if self.cbEduardo.isChecked():
            print("eduardo true")
            self.eduardo = "Eduardo\n"
        else:
            print("eduardo false")
            self.eduardo = " "
        self.txtEquipo.setPlainText(self.uriel + self.badillo + self.eduardo + self.sofi)

    def selfBadillo(self):
        if self.cbBadillo.isChecked():
            print("badillo true")
            self.badillo = "Badillo\n"

        else:
            print("badillo false")
            self.badillo = " "
        self.txtEquipo.setPlainText(self.uriel +self.badillo+self.eduardo+self.sofi)

    def selfSofi(self):
        if self.cbSofi.isChecked():
            print("sofi true")
            self.sofi = "Sofi\n"

        else:
            print("sofi false")
            self.sofi = " "
        self.txtEquipo.setPlainText(self.uriel + self.badillo + self.eduardo + self.sofi)

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

