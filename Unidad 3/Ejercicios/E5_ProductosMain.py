# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E5_ProductosMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1286, 573)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 239);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 181, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/logo uat.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1110, 0, 181, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/logo fians.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1110, 430, 181, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Logos/Imagenes/equipo.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.txtExistencia1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia1.setGeometry(QtCore.QRect(30, 190, 113, 41))
        self.txtExistencia1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia1.setObjectName("txtExistencia1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnCompras = QtWidgets.QPushButton(self.centralwidget)
        self.btnCompras.setGeometry(QtCore.QRect(462, 397, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCompras.setFont(font)
        self.btnCompras.setStyleSheet("background-color: rgb(255, 224, 235);")
        self.btnCompras.setObjectName("btnCompras")
        self.txtExistencia2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia2.setGeometry(QtCore.QRect(150, 190, 113, 41))
        self.txtExistencia2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia2.setObjectName("txtExistencia2")
        self.txtExistencia4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia4.setGeometry(QtCore.QRect(390, 190, 113, 41))
        self.txtExistencia4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia4.setObjectName("txtExistencia4")
        self.txtExistencia3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia3.setGeometry(QtCore.QRect(270, 190, 113, 41))
        self.txtExistencia3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia3.setObjectName("txtExistencia3")
        self.txtExistencia7 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia7.setGeometry(QtCore.QRect(750, 190, 113, 41))
        self.txtExistencia7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia7.setObjectName("txtExistencia7")
        self.txtExistencia8 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia8.setGeometry(QtCore.QRect(870, 190, 113, 41))
        self.txtExistencia8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia8.setObjectName("txtExistencia8")
        self.txtExistencia6 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia6.setGeometry(QtCore.QRect(630, 190, 113, 41))
        self.txtExistencia6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia6.setObjectName("txtExistencia6")
        self.txtExistencia5 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia5.setGeometry(QtCore.QRect(510, 190, 113, 41))
        self.txtExistencia5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia5.setObjectName("txtExistencia5")
        self.txtExistencia9 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia9.setGeometry(QtCore.QRect(990, 190, 113, 41))
        self.txtExistencia9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia9.setObjectName("txtExistencia9")
        self.txtExistencia10 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtExistencia10.setGeometry(QtCore.QRect(1110, 190, 113, 41))
        self.txtExistencia10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtExistencia10.setObjectName("txtExistencia10")
        self.txtPedido10 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido10.setGeometry(QtCore.QRect(1110, 310, 113, 41))
        self.txtPedido10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido10.setObjectName("txtPedido10")
        self.txtPedido5 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido5.setGeometry(QtCore.QRect(510, 310, 113, 41))
        self.txtPedido5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido5.setObjectName("txtPedido5")
        self.txtPedido7 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido7.setGeometry(QtCore.QRect(750, 310, 113, 41))
        self.txtPedido7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido7.setObjectName("txtPedido7")
        self.txtPedido6 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido6.setGeometry(QtCore.QRect(630, 310, 113, 41))
        self.txtPedido6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido6.setObjectName("txtPedido6")
        self.txtPedido3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido3.setGeometry(QtCore.QRect(270, 310, 113, 41))
        self.txtPedido3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido3.setObjectName("txtPedido3")
        self.txtPedido9 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido9.setGeometry(QtCore.QRect(990, 310, 113, 41))
        self.txtPedido9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido9.setObjectName("txtPedido9")
        self.txtPedido4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido4.setGeometry(QtCore.QRect(390, 310, 113, 41))
        self.txtPedido4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido4.setObjectName("txtPedido4")
        self.txtPedido2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido2.setGeometry(QtCore.QRect(150, 310, 113, 41))
        self.txtPedido2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido2.setObjectName("txtPedido2")
        self.txtPedido8 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido8.setGeometry(QtCore.QRect(870, 310, 113, 41))
        self.txtPedido8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido8.setObjectName("txtPedido8")
        self.txtPedido1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPedido1.setGeometry(QtCore.QRect(30, 310, 113, 41))
        self.txtPedido1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPedido1.setObjectName("txtPedido1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1286, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Existencias"))
        self.label_5.setText(_translate("MainWindow", "Pedidos"))
        self.btnCompras.setText(_translate("MainWindow", "Calcular Compras"))
import recursos_rc

