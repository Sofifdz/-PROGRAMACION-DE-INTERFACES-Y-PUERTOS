# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plantilla_Grafica.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FiguraCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as BarraNavegacion

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1402, 837)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_graficar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graficar.setGeometry(QtCore.QRect(390, 180, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_graficar.setFont(font)
        self.btn_graficar.setObjectName("btn_graficar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 170, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_polinomio = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_polinomio.setGeometry(QtCore.QRect(160, 180, 171, 31))
        self.txt_polinomio.setObjectName("txt_polinomio")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-80, 220, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.txt_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_titulo.setGeometry(QtCore.QRect(160, 230, 171, 31))
        self.txt_titulo.setObjectName("txt_titulo")
        self.btn_titulo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_titulo.setGeometry(QtCore.QRect(390, 310, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_titulo.setFont(font)
        self.btn_titulo.setObjectName("btn_titulo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-30, 320, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.btn_grilla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_grilla.setGeometry(QtCore.QRect(170, 330, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_grilla.setFont(font)
        self.btn_grilla.setObjectName("btn_grilla")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 480, 611, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpiar.setGeometry(QtCore.QRect(590, 140, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(620, 210, 201, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 230, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(930, 60, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(990, 660, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cb_estiloLinea = QtWidgets.QComboBox(self.centralwidget)
        self.cb_estiloLinea.setGeometry(QtCore.QRect(680, 360, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cb_estiloLinea.setFont(font)
        self.cb_estiloLinea.setObjectName("cb_estiloLinea")
        self.cb_ColorLinea = QtWidgets.QComboBox(self.centralwidget)
        self.cb_ColorLinea.setGeometry(QtCore.QRect(940, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cb_ColorLinea.setFont(font)
        self.cb_ColorLinea.setObjectName("cb_ColorLinea")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(900, 170, 20, 521))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(980, 180, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(980, 240, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(980, 310, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.sp_Xmin = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_Xmin.setGeometry(QtCore.QRect(1220, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_Xmin.setFont(font)
        self.sp_Xmin.setObjectName("sp_Xmin")
        self.sp_Xmax = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_Xmax.setGeometry(QtCore.QRect(1230, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_Xmax.setFont(font)
        self.sp_Xmax.setObjectName("sp_Xmax")
        self.sp_divisionesX = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_divisionesX.setGeometry(QtCore.QRect(1260, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_divisionesX.setFont(font)
        self.sp_divisionesX.setObjectName("sp_divisionesX")
        self.sp_divisionesY = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_divisionesY.setGeometry(QtCore.QRect(1260, 560, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_divisionesY.setFont(font)
        self.sp_divisionesY.setObjectName("sp_divisionesY")
        self.sp_Ymin = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_Ymin.setGeometry(QtCore.QRect(1250, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_Ymin.setFont(font)
        self.sp_Ymin.setObjectName("sp_Ymin")
        self.sp_Ymax = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_Ymax.setGeometry(QtCore.QRect(1250, 490, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_Ymax.setFont(font)
        self.sp_Ymax.setObjectName("sp_Ymax")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1000, 480, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1000, 400, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1000, 560, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(920, 380, 391, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(560, 170, 20, 201))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1260, 680, 161, 111))
        self.label_4.setStyleSheet("border: 5px solid brown;\n"
"border-radius: 10px;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/equipo.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1220, 0, 161, 111))
        self.label_14.setStyleSheet("border: 5px solid brown;\n"
"border-radius: 10px;")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/logo fians.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 161, 111))
        self.label_15.setStyleSheet("border: 5px solid brown;\n"
"border-radius: 10px;")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/logo uat.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.sp_anchoLinea = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_anchoLinea.setGeometry(QtCore.QRect(990, 740, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sp_anchoLinea.setFont(font)
        self.sp_anchoLinea.setObjectName("sp_anchoLinea")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(920, 620, 391, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1402, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FiguraCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)
        # para referir al mismo axes

        self.toolbar = BarraNavegacion(self.canvas, self)

        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.toolbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_graficar.setText(_translate("MainWindow", "Graficar"))
        self.label.setText(_translate("MainWindow", "Polinomio: "))
        self.label_2.setText(_translate("MainWindow", "Título: "))
        self.btn_titulo.setText(_translate("MainWindow", "Establecer"))
        self.label_3.setText(_translate("MainWindow", "Grilla: "))
        self.btn_grilla.setText(_translate("MainWindow", "OFF"))
        self.btn_limpiar.setText(_translate("MainWindow", "LIMPIAR GRÁFICO"))
        self.label_5.setText(_translate("MainWindow", "Estilo de la Línea"))
        self.label_6.setText(_translate("MainWindow", "Color de la Línea:"))
        self.label_7.setText(_translate("MainWindow", "Ancho de la Línea "))
        self.label_8.setText(_translate("MainWindow", "Xmin:"))
        self.label_9.setText(_translate("MainWindow", "Xmax:"))
        self.label_12.setText(_translate("MainWindow", "T. Divisiones: "))
        self.label_10.setText(_translate("MainWindow", "Ymax:"))
        self.label_11.setText(_translate("MainWindow", "Ymin:"))
        self.label_13.setText(_translate("MainWindow", "T. Divisiones: "))
import recursos_rc
