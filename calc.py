# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from calculus import Ui_Calculus
from egyenlet import Ui_Egyenlet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox
import math
import re

class Ui_MainWindow(object):
    def generateWindow(self, index):
        window_type = self.comboBox.itemText(index)
        if window_type == "Kalkulus":
            self.generateKalkulus()
            MainWindow.hide()
        if window_type == "Egyenletek":
            self.generateEgyenlet()
            MainWindow.hide()

    def generateKalkulus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Calculus()
        self.ui.setupUi(self.window, MainWindow)
        self.window.show()

    def generateEgyenlet(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Egyenlet()
        self.ui.setupUi(self.window, MainWindow)
        self.window.show()

    def setupUi(self, MainWindow):

        #toolbar combobox
        self.toolbar = MainWindow.addToolBar("My Toolbar")

        # Create a combobox
        font = QFont()
        font.setPointSize(12)  # Set the desired font size

        self.comboBox = QComboBox()
        self.comboBox.setFont(font)
        self.comboBox.addItems(["Válasz egyet:", "Kalkulus", "Egyenletek", "Differnciál számitás"])
        self.comboBox.currentIndexChanged.connect(self.generateWindow)

        # Add the combobox to the toolbar
        self.toolbar.addWidget(self.comboBox)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(13, 10, 504, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.outputLabel.setFont(font)
        self.outputLabel.setAutoFillBackground(True)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")

        self.percentageButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("%"))
        self.percentageButton.setGeometry(QtCore.QRect(14, 120, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentageButton.setFont(font)
        self.percentageButton.setObjectName("percentageButton")

        self.clearEntryButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("CE"))
        self.clearEntryButton.setGeometry(QtCore.QRect(139, 120, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearEntryButton.setFont(font)
        self.clearEntryButton.setObjectName("clearEntryButton")

        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("C"))
        self.clearButton.setGeometry(QtCore.QRect(264, 120, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.delete())
        self.deleteButton.setGeometry(QtCore.QRect(389, 120, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.quadratButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.quadrat())
        self.quadratButton.setGeometry(QtCore.QRect(139, 200, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.quadratButton.setFont(font)
        self.quadratButton.setObjectName("quadratButton")
        self.onePerXButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.one_per_x())
        self.onePerXButton.setGeometry(QtCore.QRect(14, 200, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.onePerXButton.setFont(font)
        self.onePerXButton.setObjectName("onePerXButton")
        self.sqrtButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.sqrt_func())
        self.sqrtButton.setGeometry(QtCore.QRect(264, 200, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sqrtButton.setFont(font)
        self.sqrtButton.setObjectName("sqrtButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(389, 200, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("7"))
        self.Button_7.setGeometry(QtCore.QRect(14, 280, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("8"))
        self.Button_8.setGeometry(QtCore.QRect(139, 280, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(389, 280, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("9"))
        self.Button_9.setGeometry(QtCore.QRect(264, 280, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("5"))
        self.Button_5.setGeometry(QtCore.QRect(139, 360, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(389, 360, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("4"))
        self.Button_4.setGeometry(QtCore.QRect(14, 360, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("6"))
        self.Button_6.setGeometry(QtCore.QRect(264, 360, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("2"))
        self.Button_2.setGeometry(QtCore.QRect(139, 440, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("3"))
        self.Button_3.setGeometry(QtCore.QRect(264, 440, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(389, 440, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("1"))
        self.Button_1.setGeometry(QtCore.QRect(14, 440, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.plusMinusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.plus_minus())
        self.plusMinusButton.setGeometry(QtCore.QRect(14, 520, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setObjectName("plusMinusButton")
        self.decimalPointButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.dot())
        self.decimalPointButton.setGeometry(QtCore.QRect(264, 520, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalPointButton.setFont(font)
        self.decimalPointButton.setObjectName("decimalPointButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(139, 520, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.equal())
        self.equalButton.setGeometry(QtCore.QRect(389, 520, 126, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            #Check to see if it starts with 0 and delete the zero
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            #concatenate the pressed button with what was there already
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def dot(self):
        screen = self.outputLabel.text()
        
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')
    
    def delete(self):
        if  len(self.outputLabel.text()) > 1:
            self.outputLabel.setText(self.outputLabel.text()[:-1])
        elif len(self.outputLabel.text()) == 1:
            self.outputLabel.setText("0")
    
    def plus_minus(self):
        original = self.outputLabel.text()
        #print(self.contains_only_one_number(original))

        if self.contains_only_one_number(original) and original[0] != "-":
            res = "-" + original[0:]
            self.outputLabel.setText(res)
            
        if self.contains_only_one_number(original) and original[0] == "-":
            res = original[1:]
            self.outputLabel.setText(res)
        
        if self.contains_only_one_float(original) and original[0] != "-":
            res = "-" + original[0:]
            self.outputLabel.setText(res)
            
        if self.contains_only_one_float(original) and original[0] == "-":
            res = original[1:]
            self.outputLabel.setText(res)

    def equal(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            if type(answer) is int:
                self.outputLabel.setText(str(answer))
            else:
                self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("Error")
    
    def quadrat(self):
        try:
            original = self.outputLabel.text()
            self.outputLabel.setText(str(float(original) * float(original)) )
        except:
            self.outputLabel.setText("ERROR")

    def sqrt_func(self):
        try:
            original = self.outputLabel.text()
            self.outputLabel.setText(str(round(math.sqrt(float(original)), 2)))
        except:
            self.outputLabel.setText("ERROR")               

    def one_per_x(self):
        original = float(self.outputLabel.text())
        self.outputLabel.setText(str(round((1 / original), 2)))
    
    def last_number(self, string):
        i = len(string) - 1
        while i >= 0 and string[i].isdigit():
            i -= 1
        return string[i+1:]

    def contains_only_one_number(self, input_str):
        pattern = r'^\D*\d+\D*$'
        return bool(re.match(pattern, input_str))

    def contains_only_one_float(self,input_str):
        try:
            float_value = float(input_str)
            return True
        except ValueError:
            return False
        
    def last_float_number(self, input_str):
        float_numbers = re.findall(r"[-+]?\d*\.\d+|\d+", input_str)
        if float_numbers:
            return float(float_numbers[-1])
        else:
            return None


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentageButton.setText(_translate("MainWindow", "%"))
        self.clearEntryButton.setText(_translate("MainWindow", "CE"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.deleteButton.setText(_translate("MainWindow", "DEL"))
        self.quadratButton.setText(_translate("MainWindow", "x²"))
        self.onePerXButton.setText(_translate("MainWindow", "1/x"))
        self.sqrtButton.setText(_translate("MainWindow", "sqrt(2)"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.multiplyButton.setText(_translate("MainWindow", "*"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.decimalPointButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
