import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P13_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#ACTUALIZAR IMAGENES :pyrcc5 recursos.qrc -o recursos_rc.py

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)



        # Área de los Signals
        self.rbUriel.clicked.connect(self.clicUriel)
        self.rbEduardo.toggled.connect(self.clicEduardo)
        self.rbBadillo.clicked.connect(self.clicBadillo)
        self.rbSofia.clicked.connect(self.clicSofia)

        self.uriel = " "
        self.eduardo = " "
        self.badillo = " "
        self.sofi = " "

    def clicUriel(self):
        print("histe clic uriel")

    def clicEduardo(self):
       print("hisiste clic a eduardo")
    def clicBadillo(self):
        if self.cbBadillo.isChecked():
            print("badillo true")
            self.badillo = "Badillo\n"

        else:
            print("badillo false")
            self.badillo = " "
        self.txtEquipo.setPlainText(self.uriel +self.badillo+self.eduardo+self.sofi)

    def clicSofia(self):
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

