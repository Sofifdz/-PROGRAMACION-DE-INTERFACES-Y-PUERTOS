import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.datos_alumnos = {
            1: ["Sofia Mariana Fernandez Arrazola", "Dormir", 5, "A+", ":/Variadas/Imagenes/sofi.png"],
            2: ["Eduardo Juarez Beltran", "Jugar", 5, "B+", ":/Variadas/Imagenes/JuarezBeltran.png"],
            3: ["Uriel Gonzalez Gabriel", "Jugar", 5, "C+", ":/Variadas/Imagenes/GonzalezUriel.png"],
            4: ["Victor Manuel badillo Gonzalez", "Jugar", 5, "D+", ":/Variadas/Imagenes/badillo .png"],
        }
        self.cbEquipo.addItem("Selecciona...", 0)
        self.cbEquipo.addItem("Sofia",1)
        self.cbEquipo.addItem("Eduardo", 2)
        self.cbEquipo.addItem("Uriel", 3)
        self.cbEquipo.addItem("Badillo", 4)

        self.cbEquipo.currentIndexChanged.connect(self.cambia)


    def cambia(self):
        try:
            print("Text: "+self.cbEquipo.currentText())
            print("Index: " + str(self.cbEquipo.currentIndex()))
            print("Data: " + str(self.cbEquipo.currentData()))

            dataClave = self.cbEquipo.currentData()
            imagen = self.datos_alumnos[dataClave][-1]
            self.imgPersona.setPixmap(QtGui.QPixmap(imagen))
        except Exception as error:
         print(error)

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
