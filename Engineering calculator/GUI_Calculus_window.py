# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculus.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Helper_class_Plotting import Canvas
from sympy import (
    oo,
    Sum,
    Symbol,
    Interval,
    sympify,
    limit,
    integrate,
    is_increasing,
    is_strictly_increasing,
    is_decreasing,
    is_monotonic,
    is_strictly_decreasing,
    diff,
)
from sympy import (
    sin,
    cos,
    tan,
    log,
    atan,
    asin,
    acos,
    asinh,
    acosh,
    atanh,
    sinh,
    cosh,
    tanh,
    exp,
    Abs,
    sign,
    sqrt,
    sec,
    csc,
    pi,
    E
)
import re
from math import pi


class Ui_Calculus(object):
    def extract_variable(self, expression):
        pattern = r"[a-zA-Z]+"

        matches = re.findall(pattern, expression)

        if matches:
            return matches[0]
        else:
            return None

    def has_no_variables(self, func_str):
        # Define a regular expression pattern to match mathematical variables
        var_pattern = r"[a-zA-Z]+"
        # Find all matches of variables in the function string
        variables = re.findall(var_pattern, func_str)
        # If no variables are found, return True
        return len(variables) == 0

    def replace_sympy_funcs(self, func_str):
        replacements = {
            r"\b(ln)\b": "log",
            # trig
            r"\bsin\b": "sin",
            r"\bcos\b": "cos",
            r"\btan\b": "tan",
            # Inverse trig
            r"\barctan\b": "atan",
            r"\barcsin\b": "asin",
            r"\barccos\b": "acos",
            # Inverse hyperbolic
            r"\barcsinh\b": "asinh",
            r"\barccosh\b": "acosh",
            r"\barctanh\b": "atanh",
            # hyperbolic
            r"\bsinh\b": "sinh",
            r"\bcosh\b": "cosh",
            r"\btanh\b": "tanh",
            # exp
            r"\bexp\b": "exp",
            # abs
            r"\babs\b": "Abs",
            # sign(x)
            r"\sign\b": "sign",
            # sqrt
            r"\bsqrt\b": "sqrt",
            # secant and cosecant
            r"\bsec\b": "sec",
            r"\bcsc\b": "csc",
            #pi and e
            r"\bpi\b": "pi",
            r"\be\b": "E"
        }

        for pattern, np_func in replacements.items():
            func_str = re.sub(pattern, np_func, func_str)

        func_str = func_str.replace("^", "**")

        return func_str

    def combobox_selector(self):
        also = 0
        felso = 0

        # pi
        if "pi" in self.lineEdit_2.text() or "pi" in self.lineEdit_3.text():
            print("#LOG PI")
            try:
                if "pi" in self.lineEdit_2.text() and " " in self.lineEdit_2.text():
                    also = int(int(self.lineEdit_2.text().split(" ")[0]) * pi)
                    print("also if:", also)
                elif "pi" in self.lineEdit_2.text() and not " " in self.lineEdit_2.text():
                    also = int(int(self.lineEdit_2.text().split("pi")[0]) * pi)
                    print("also else:", also)
                else:
                    also = int(self.lineEdit_2.text())

                if "pi" in self.lineEdit_3.text() and " " in self.lineEdit_3.text():
                    felso = int(int(self.lineEdit_3.text().split("pi")[0]) * pi)
                    print("felso if:", felso)
                elif "pi" in self.lineEdit_3.text() and not " " in self.lineEdit_3.text():
                    felso = int(int(self.lineEdit_3.text().split("pi")[0]) * pi)
                    print("felso else:", felso)
                else:
                    felso = int(self.lineEdit_3.text())
            except:
                self.label_2.setText("ERROR rossz határ megadás pi-vel")
                self.lineEdit_2.setText("-10")
                self.lineEdit_2.setText("10")
            interval = (also, felso)
        elif self.lineEdit_2.text().replace("-", "").isdigit() and self.lineEdit_3.text().isdigit():
            print("#LOG Másik ág")
            also = sympify(self.lineEdit_2.text())
            felso = sympify(self.lineEdit_3.text())
            # inf
            if sympify(self.lineEdit_2.text()) == -oo:
                also = -1000000000

            if sympify(self.lineEdit_3.text()) == oo:
                felso = 1000000000

            # zero
            if sympify(self.lineEdit_2.text()) == 0:
                also = 0

            if sympify(self.lineEdit_3.text()) == 0:
                felso = 0

            # not zero
            if sympify(self.lineEdit_2.text()) != 0:
                also = float(also)

            if sympify(self.lineEdit_3.text()) != 0:
                felso = float(felso)
            interval = (also, felso)
        else:
            self.label_2.setText("ERROR: nem jó határok")
            self.lineEdit_2.setText("-10")
            self.lineEdit_3.setText("10")
            self.canvas.clear(interval_x=interval, interval_y=interval)
        input = self.comboBox.currentText()
        text = self.lineEdit.text()
        x = Symbol("x", real=True)
        
        if input == "Növekvő":
            try:
                res = is_increasing(sympify(self.replace_sympy_funcs(text)), Interval(also,felso))
                if res == True:
                    self.label_2.setText(text + " növekvő")
                else:
                    self.label_2.setText(text + " nem növekvő")
                result = self.canvas.plot_function(func_str=text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Növekvő függvény!")

        if input == "Szigorúan növekvő":
            try:
                res = is_strictly_increasing(
                    sympify(self.replace_sympy_funcs(text)), Interval(also, felso)
                )
                if res == True:
                    self.label_2.setText(text + " szigorúan növekvő")
                else:
                    self.label_2.setText(text + " szigorúan nem növekvő")
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Szigorúan növekvő függvény!")

        if input == "Csökkenő":
            try:
                res = is_decreasing(
                    sympify(self.replace_sympy_funcs(text)), Interval(also, felso)
                )
                if res == True:
                    self.label_2.setText(text + " Csökkenő")
                else:
                    self.label_2.setText(text + " nem csökkenő")
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Csökkenő függvény!")

        if input == "Szigorúan csökkenő":
            try:
                res = is_strictly_decreasing(
                    sympify(self.replace_sympy_funcs(text)), Interval(also, felso)
                )
                if res == True:
                    self.label_2.setText(text + " szigorúan csökkenő")
                else:
                    self.label_2.setText(text + " szigorúan nem csökkenő")
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Szigorúan csökkenő függvény!")

        if input == "Monoton":
            try:
                res = is_monotonic(
                    sympify(self.replace_sympy_funcs(text)), Interval(also, felso)
                )
                if res == True:
                    self.label_2.setText(text + " Monoton")
                else:
                    self.label_2.setText(text + " nem monoton")
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Monoton függvény!")

        if input == "Divergens":
            try:
                res = limit(sympify(text), x, oo)
                if res == oo:
                    self.label_2.setText(text + " Divergens")
                else:
                    self.label_2.setText(text + " Nem divergens")
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Divergens függvény!")
            
        if input == "Határérték":
            try:
                if self.has_no_variables(text):
                    self.label_2.setText(text + " -> " + str(eval(text)))
                else:
                    res = limit(sympify(text), x, oo)
                    self.label_2.setText(text + " -> " + str(res))
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Határérték függvény!")

        if input == "Konvergens":
            try:
                res = Sum(self.replace_sympy_funcs(text), (x, also, felso)).is_convergent()
                if res:
                    self.label_2.setText(text + " a sorozat konvergál.")
                else:
                    self.label_2.setText(text + " a sorozat nem konvergál.")
                result = self.canvas.plot_function(text, interval_x=interval, interval_y=interval)
                if result == False:
                    self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Konvergens függvény!")

        if input == "Deriválás":
            try:
                tmp = eval(self.replace_sympy_funcs(text))
                print(tmp)
                res = diff((tmp), x)
                self.label_2.setText(str(res).replace("E", "e"))
                res_str = str(res).replace("E", "e")
                result = self.canvas.plot_function(res_str, interval_x=interval, interval_y=interval)
                if result == False:
                    #self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Deriválás!")
            

        if input == "Integrálás":
            try:
                x = Symbol("x")
                res = integrate(self.replace_sympy_funcs(text), x)
                self.label_2.setText(str(res).replace("**", "^").replace("E", "e") + " + C")
                res_str = str(res).replace("E", "e")
                result = self.canvas.plot_function(res_str, interval_x=interval, interval_y=interval)
                if result == False:
                    #self.label_2.setText("ERROR: hibás függvény!")
                    self.lineEdit.setText("")
            except Exception as e:
                print(e)
                self.label_2.setText("ERROR helytelen Integrálás!")
        self.pushButton.setEnabled(False)
        # except:
        #     self.label_2.setText("ERROR helytelen függvény!")

    def back_to_mainwindow(self, Egyenlet, MainWindow):
        Egyenlet.close()
        MainWindow.show()
    
    def on_text_changed(self, text):
        self.pushButton.setEnabled(bool(text.strip()))

    def setupUi(self, Calculus, MainWindow):

        self.applyStylesheet(Calculus)

        Calculus.setObjectName("Calculus")
        Calculus.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Calculus)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("-10")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("10")

        self.pushButton_2 = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.back_to_mainwindow(Calculus, MainWindow),
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Vissza")

        self.canvas = Canvas(self.centralwidget)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Növekvő")
        self.comboBox.addItem("Szigorúan növekvő")
        self.comboBox.addItem("Csökkenő")
        self.comboBox.addItem("Szigorúan csökkenő")
        self.comboBox.addItem("Monoton")
        self.comboBox.addItem("Divergens")
        self.comboBox.addItem("Határérték")
        self.comboBox.addItem("Konvergens")
        self.comboBox.addItem("Deriválás")
        self.comboBox.addItem("Integrálás")

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Válaszd ki a végrehajtandó műveletet")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Erdemény")
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.on_text_changed)

        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.combobox_selector()
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Enter")
        self.pushButton.setEnabled(False)  # Initially disable the button

        # Create layouts
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        form_layout = QtWidgets.QHBoxLayout()
        form_layout.addWidget(self.label)
        form_layout.addWidget(self.lineEdit_2)
        form_layout.addWidget(self.lineEdit_3)

        input_layout = QtWidgets.QHBoxLayout()
        input_layout.addWidget(self.comboBox)
        input_layout.addWidget(self.lineEdit)
        input_layout.addWidget(self.pushButton)

        result_layout = QtWidgets.QVBoxLayout()
        result_layout.addWidget(self.label_2)

        canvas_layout = QtWidgets.QVBoxLayout()
        canvas_layout.addWidget(self.canvas)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.pushButton_2)

        # Add layouts to main layout
        main_layout.addLayout(form_layout)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(result_layout)
        main_layout.addLayout(canvas_layout)
        main_layout.addLayout(button_layout)

        Calculus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Calculus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculus)
        self.statusbar.setObjectName("statusbar")
        Calculus.setStatusBar(self.statusbar)

        self.retranslateUi(Calculus)
        QtCore.QMetaObject.connectSlotsByName(Calculus)

    def applyStylesheet(self, Calculus):
        stylesheet = """
        QMainWindow {
            background-color: #2E2E2E;
        }
        QLabel#label_2 {
            background-color: #1C1C1C;
            font-family: 'Courier New', Courier, monospace;
            color: #FFFFFF;
            border: 2px solid #555555;
            border-radius: 5px;
            padding: 10px;
        }
        QLabel#label {
            background-color: #1C1C1C;
            font-size: 12pt;
            font-family: 'Courier New', Courier, monospace;
            color: #FFFFFF;
        }
        QLineEdit#lineEdit_2, QLineEdit#lineEdit_3, QLineEdit#lineEdit {
            background-color: #1C1C1C;
            font-family: 'Courier New', Courier, monospace;
            color: #FFFFFF;
            font-size: 10pt;
            width: 35px;
            height: 30%;
        }
        QPushButton {
            background-color: #4E4E4E;
            font-family: 'Courier New', Courier, monospace;
            color: #FFFFFF;
            font-size: 12pt;
            border: 1px solid #555555;
            border-radius: 10px;
            padding: 10px;
            width: 50px;
            height: 35%;
        }
        QPushButton#pushButton_2 {
            width: 60px;
            height: 40%;
        }
        QPushButton:hover {
            background-color: #5E5E5E;
        }
        QPushButton:pressed {
            background-color: #6E6E6E;
        }
        QComboBox {
            background-color: #4E4E4E;
            font-family: 'Courier New', Courier, monospace;
            color: #FFFFFF;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 5px;
        }
        QComboBox#comboBox {
        font-family: 'Courier New', Courier, monospace;
        width: 330px;
        }
        QComboBox QAbstractItemView {
            font-family: 'Courier New', Courier, monospace;
            background-color: #4E4E4E;
            selection-background-color: #5E5E5E;
            color: #FFFFFF;
        }
        QToolBar {
            background-color: #3E3E3E;
            font-family: 'Courier New', Courier, monospace;
            border: none;
        }
        """
        Calculus.setStyleSheet(stylesheet)

    def retranslateUi(self, Calculus):
        _translate = QtCore.QCoreApplication.translate
        Calculus.setWindowTitle(_translate("Calculus", "Calculus"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Calculus = QtWidgets.QMainWindow()
    ui = Ui_Calculus()
    ui.setupUi(Calculus)
    Calculus.show()
    sys.exit(app.exec_())
