
import sys
from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile3 = "ventana2.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)
class MyDialog(QtWidgets.QDialog,Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)



qtCreatorFile3 = "ventana1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_sumar.clicked.connect(self.sumar)

        # Área de los Signals

    # Área de los Slots
    def sumar(self):
      a = int(self.txt_A.text())
      b = int(self.txt_B.text())
      r = a+b

      self.dialogo = MyDialog()
      self.dialogo.setModal(False)
      self.dialogo.text_resultado.setText(str(r))
      self.dialogo.show()




##################################################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())