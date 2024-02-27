import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P1_DescripcioImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_alumnos = {
            1:["Sofia Mariana Fernandez Arrazola","Dormir",5,"A+",":/Variadas/Imagenes/sofi.png"],
            2: ["Eduardo Juarez Beltran", "Jugar", 5, "B+",":/Variadas/Imagenes/JuarezBeltran.png"],
            3: ["Uriel Gonzalez Gabriel", "Jugar", 5, "C+",":/Variadas/Imagenes/GonzalezUriel.png"],
            4: ["Victor Manuel badillo Gonzalez", "Jugar", 5, "D+",":/Variadas/Imagenes/badillo .png"],
        }

        self.btnAtras.clicked.connect(self.atras)
        self.btnAdelante.clicked.connect(self.adelante)
        self.index_control = 0
        self.btnAtras.setEnabled(False)

    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_alumnos[self.index_control]
            print(datos)
            self.btnAdelante.setEnabled(True)

            self.imgPersonas.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 1:
            self.btnAtras.setEnabled(False)


    def adelante(self):
        if self.index_control < 4:
            self.btnAtras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_alumnos[self.index_control]
            print(datos)
            self.imgPersonas.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 4:
            self.btnAdelante.setEnabled(False)


    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
