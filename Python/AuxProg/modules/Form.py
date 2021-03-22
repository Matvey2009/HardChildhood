# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0uNwxAy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(111, 61)
        icon = QIcon()
        icon.addFile(u"D:/Documents/Pictures/\u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 111, 61))
        self.pushButton.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 4px solid rgb(255, 0, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Fon = QGraphicsView(Form)
        self.Fon.setObjectName(u"Fon")
        self.Fon.setGeometry(QRect(-20, -20, 256, 192))
        self.Fon.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.318182 rgba(5, 5, 5, 255), stop:0.965909 rgba(255, 255, , 255));\n"
"}")
        self.Fon.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AuxProg", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0436\u0438\u043c\u0430\u0439 \u0441\u044e\u0434\u0430", None))
    # retranslateUi

