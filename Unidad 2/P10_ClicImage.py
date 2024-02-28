from QLabelClickeable import clickable

import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P10_ClicImage.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #self.img.clicked.connect(self.clicImage) #No se puede con labels
        clickable(self.img).connect(self.clicImage)

        self.btn_borrar.clicked.connect(self.borrar)

    def clicImage(self):
        print("Hiciste clic")
        self.txt_Nombre.setText("Kenia Os")
        self.txt_Edad.setText("24")
        self.txt_Ocupacion.setText("Cantante¡¡¡!!!")

    def borrar(self,event):

            reply = QtWidgets.QMessageBox.warning(self, "Mensaje", "Seguro que quieres borrar la info de la kenini?", QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.txt_Nombre.setText("")
                self.txt_Edad.setText("")
                self.txt_Ocupacion.setText("")
            else:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("¡¡¡BIENVENIDO KENINI!!!")
                resp = msgBox.exec_()
                print("Respuesta: ", resp)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())