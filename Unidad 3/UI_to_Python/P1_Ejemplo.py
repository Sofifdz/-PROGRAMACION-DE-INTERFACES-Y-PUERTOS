# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P1_Ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 437)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 330, 111, 71))
        self.label_3.setStyleSheet("border: 5px solid black;\n"
"border-radius: 10px;\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/equipo.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 20, 111, 71))
        self.label_2.setStyleSheet("border: 5px solid red;\n"
"border-radius: 10px;\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/logo fians.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 71))
        self.label_4.setStyleSheet("border: 5px solid white;\n"
"border-radius: 10px;\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/logo uat.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.txtRecomendacion = QtWidgets.QLabel(self.centralwidget)
        self.txtRecomendacion.setGeometry(QtCore.QRect(70, 530, 721, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(11)
        self.txtRecomendacion.setFont(font)
        self.txtRecomendacion.setText("")
        self.txtRecomendacion.setObjectName("txtRecomendacion")
        self.nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(270, 110, 221, 61))
        self.nombre.setObjectName("nombre")
        self.btn_saludar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saludar.setGeometry(QtCore.QRect(290, 230, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_saludar.setFont(font)
        self.btn_saludar.setObjectName("btn_saludar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nombre.setText(_translate("MainWindow", "H"))
        self.btn_saludar.setText(_translate("MainWindow", "SALUDO"))
import recursos_rc
