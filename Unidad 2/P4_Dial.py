import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P4_Dial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.dialinfPersona = {
            1: ["Sofia Mariana Fernandez Arrazola", "Dormir", 5, "A+", ":/Variadas/Imagenes/sofi.png"],
            2: ["Eduardo Juarez Beltran", "Jugar", 5, "B+", ":/Variadas/Imagenes/JuarezBeltran.png"],
            3: ["Uriel Gonzalez Gabriel", "Jugar", 5, "C+", ":/Variadas/Imagenes/GonzalezUriel.png"],
            4: ["Victor Manuel badillo Gonzalez", "Jugar", 5, "D+", ":/Variadas/Imagenes/badillo .png"],
        }

        self.dialPersonas.setMinimum(0)
        self.dialPersonas.setMaximum(len(self.dialinfPersona))
        self.dialPersonas.setSingleStep(1)
        self.dialPersonas.setValue(0)
        self.dialPersonas.valueChanged.connect(self.cambia)

    def cambia(self):
        selected_value = self.dialPersonas.value()
        print(selected_value)

        if selected_value in self.dialinfPersona:
            data = self.dialinfPersona[selected_value]
            image_path = data[-1]
            self.imgPersona.setPixmap(QtGui.QPixmap(image_path))
        else:
            print("Selected value not found in personData.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
