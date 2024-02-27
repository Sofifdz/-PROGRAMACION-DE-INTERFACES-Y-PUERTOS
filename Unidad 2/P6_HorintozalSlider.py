import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P6_HorizontalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_personas = {
            1: ["Sofia Mariana Fernandez Arrazola", "Dormir", 5, "A+", ":/Variadas/Imagenes/sofi.png"],
            2: ["Eduardo Juarez Beltran", "Jugar", 5, "B+", ":/Variadas/Imagenes/JuarezBeltran.png"],
            3: ["Uriel Gonzalez Gabriel", "Jugar", 5, "C+", ":/Variadas/Imagenes/GonzalezUriel.png"],
            4: ["Victor Manuel badillo Gonzalez", "Jugar", 5, "D+", ":/Variadas/Imagenes/badillo .png"],
        }

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(4)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.valueChanged.connect(self.cambia)

    def cambia(self):

       try:
        dataClave = self.horizontalSlider.value()
        print(dataClave)
        imgpersona = self.datos_personas[dataClave][-1]
        self.imgpersona.setPixmap(QtGui.QPixmap(imgpersona))
       except Exception as error:
           print(error)


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())