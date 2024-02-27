import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VerticalSlider.ui"  # Nombre del archivo aquí.
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

        self.vs_personas.setMinimum(0)
        self.vs_personas.setMaximum(4)
        self.vs_personas.setSingleStep(1)
        self.vs_personas.setValue(0)
        self.vs_personas.valueChanged.connect(self.cambia)

    def cambia(self):

       try:
        dataClave = self.vs_personas.value()
        print(dataClave)
        imagen = self.datos_personas[dataClave][-1]
        self.img_persona_4.setPixmap(QtGui.QPixmap(imagen))
       except Exception as error:
           print(error)


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())