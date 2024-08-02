# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prob_and_stat.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import math
from matplotlib.pylab import pareto
import numpy as np
from Helper_class_Plotting import Canvas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit
from scipy import stats
import statistics
from scipy.stats import norm
from sympy import N, pretty, sympify, symbols, gamma, log, digamma, sqrt
from sympy.stats import (
    Normal,
    Geometric,
    Poisson,
    Logarithmic,
    Erlang,
    Pareto,
    P,
    E,
    variance,
    density,
    entropy,
    variance,
)


class Ui_Probability_and_statistics(object):
    def setupUi(self, Ui_Prob_and_Stat, MainWindow):
        self.applyStylesheet(Ui_Prob_and_Stat)
        Ui_Prob_and_Stat.setObjectName("Ui_Prob_and_Stat")
        Ui_Prob_and_Stat.resize(800, 600)
        Ui_Prob_and_Stat.setMinimumSize(QtCore.QSize(800, 600))
        Ui_Prob_and_Stat.setMaximumSize(QtCore.QSize(800, 600))
        Ui_Prob_and_Stat.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(Ui_Prob_and_Stat)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)

        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.handle_combobox_change)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 780, 70
                                              ))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.combobox_selector()
        )
        self.pushButton.setGeometry(QtCore.QRect(710, 40, 75, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.back_to_mainwindow(Ui_Prob_and_Stat, MainWindow),
        )
        self.pushButton_2.setGeometry(QtCore.QRect(720, 500, 75, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.canvas = Canvas(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 270, 781, 221))
        self.canvas.hide()

        self.lineEdit_2 = QTextEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 40, 281, 100))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Felétetel: X < 12")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 130, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)

        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.currentTextChanged.connect(self.handle_combobox2_change)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mu = QtWidgets.QTextEdit(self.centralwidget)
        self.mu.setGeometry(QtCore.QRect(300, 40, 104, 45))
        self.mu.setObjectName("mu")

        self.alpha = QtWidgets.QTextEdit(self.centralwidget)
        self.alpha.setGeometry(QtCore.QRect(300, 150, 104, 45))
        self.alpha.setObjectName("alpha")
        self.alpha.setPlaceholderText("alpha")
        self.alpha.hide()

        self.sigma = QtWidgets.QTextEdit(self.centralwidget)
        self.sigma.setGeometry(QtCore.QRect(300, 96, 104, 45))
        self.sigma.setObjectName("sigma")
        Ui_Prob_and_Stat.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_Prob_and_Stat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Ui_Prob_and_Stat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_Prob_and_Stat)
        self.statusbar.setObjectName("statusbar")
        Ui_Prob_and_Stat.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_Prob_and_Stat)
        QtCore.QMetaObject.connectSlotsByName(Ui_Prob_and_Stat)

    def applyStylesheet(self, Egyenlet):
        stylesheet = """
        QMainWindow {
            background-color: #2E2E2E;
        }
        QWidget#centralwidget {
            background-color: #2E2E2E;
        }
        QLabel {
            color: #FFFFFF;
        }
        QLineEdit, QComboBox {
            background-color: #4E4E4E;
            color: #FFFFFF;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            background-color: #4E4E4E;
            color: #FFFFFF;
            border: 1px solid #555555;
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #5E5E5E;
        }
        QComboBox QAbstractItemView {
            background-color: #4E4E4E;
            selection-background-color: #5E5E5E;
            color: #FFFFFF;
        }
        QPushButton:pressed {
            background-color: #6E6E6E;
        }
        """
        Egyenlet.setStyleSheet(stylesheet)

    def back_to_mainwindow(self, Egyenlet, MainWindow):
        Egyenlet.close()
        MainWindow.show()

    def string_to_S(self, string):

        return string.replace(" ", "").replace("1/", "S.One/")
    
    def number_of_lines(self, expression):
        res = []
        number = 0

        for line in expression.splitlines():
            if line.strip():
                number += 1
                res.append(line)

        return res

    def str_to_list(self, list_string):
        return [float(num) for num in list_string.split(",")]

    def t_test(self=None, mu=None, alpha=None, x=None, y=None, paired=None):

        if x is not None and mu is not None and alpha is not None:
            print("egymintás t")
            result_string = ""

            avg = statistics.mean(x)
            stan_dev = statistics.stdev(x)
            m = mu
            n = len(x)

            Alpha = 1 - alpha
            df = n - 1


            t = (avg - m) / (stan_dev / sqrt(n)) 
            t = float(t)  # Ensure numerical evaluation

            t_p = stats.t.ppf(q= Alpha/2,df= df)
            p_value = 2 * (1 - stats.t.sf(abs(float(t)), df))

            if abs(t) >= t_p:
                
                result_string += f"\nA nullhipotézist elvetjük t: {t} p: {2 - p_value}\n"
                result_string += f"two tail  p:{stats.t.ppf(q= Alpha/2,df= df)}" +"\n"
                result_string += f"one tail  p:{stats.t.ppf(q= Alpha,df= df)}" +"\n"
            elif abs(t) < t_p:
                result_string += f"\nA nullhipotézist elfogadjuk t: {t} p: {2 - p_value}\n"
                result_string += f"two tail  p:{stats.t.ppf(q= Alpha/2,df= df)}" +"\n"
                result_string += f"one tail  p:{stats.t.ppf(q= Alpha,df= df)}" +"\n"

            return result_string
        elif x is not None and y is not None and paired is True and alpha is not None:
            print("kétmintás párosított t próba")
            result_string = ""
            
            x = np.array(x)
            y = np.array(y)
            z = y - x
            N = len(z)
            korr_sz = np.std(z, ddof=1)
            Alpha = 1 - alpha
            atlag = np.mean(z)
            t_critical = stats.t.ppf(1 - Alpha, N - 1)

            if atlag > t_critical * korr_sz / np.sqrt(N):
                result_string += 'H0-t elutasítjuk\n'
            else:
                result_string += 'H0-t elfogadjuk\n'

            H, P_ertek = stats.ttest_1samp(z, 0)
            print(H, P_ertek)

            result_string += f"t: {H} p: {P_ertek}\n"
            result_string += f"two tail p: {stats.t.ppf(q=Alpha/2, df=N-1)}\n"
            result_string += f"one tail p: {stats.t.ppf(q=Alpha, df=N-1)}\n"

            return result_string
        elif (x is not None and y is not None and alpha is not None):
            print("kétmintás t")
            result_string = ""
            
            t_statistic, p_value = stats.ttest_ind(x, y)

            Alpha = 1 - alpha
            if p_value < Alpha:
                result_string += "H0-t elvetjük\n"
            else:
                result_string += "H0-t elfogadjuk\n"

            result_string += f"P: {p_value} T: {t_statistic}\n"
            result_string += f"two tail p: {stats.t.ppf(q=Alpha/2, df=(len(x) + len(y) - 2))}\n"
            result_string += f"one tail p: {stats.t.ppf(q=Alpha, df=(len(x) + len(y) - 2))}\n"

            return result_string

    def u_test(self, X=None, mu=None, sigma=None, alpha=None):
        if X is not None or mu is not None or sigma is not None or alpha is not None:
            # Sample statistics
            n = len(X)
            if n == 0:
                raise ValueError("Sample data X cannot be empty.")
                
            sample_mean = np.mean(X)

            # Calculate Z-value
            z_value = (sample_mean - mu) / (sigma / np.sqrt(n))

            # Left-tailed test
            z_critical_left = norm.ppf(alpha)
            p_value_left = norm.cdf(z_value)
            reject_null_left = "igen" if z_value < z_critical_left else "nem"
            left_test_result = f"Bal oldali próba: Kritikus Z-érték: {z_critical_left}, \nP-érték: {p_value_left}, Nullhipotézis elutasítása: {reject_null_left}"

            # Two-tailed test
            z_critical_two = norm.ppf(1 - alpha / 2)
            p_value_two = 2 * (1 - norm.cdf(abs(z_value)))
            reject_null_two = "igen" if abs(z_value) > z_critical_two else "nem"
            two_test_result = f"Kétoldali próba: Kritikus Z-érték: ±{z_critical_two}, \nP-érték: {p_value_two}, Nullhipotézis elutasítása: {reject_null_two}"

            # Right-tailed test
            z_critical_right = norm.ppf(1 - alpha)
            p_value_right = 1 - norm.cdf(z_value)
            reject_null_right = "igen" if z_value > z_critical_right else "nem"
            right_test_result = f"Jobb oldali próba: Kritikus Z-érték: {z_critical_right}, \nP-érték: {p_value_right}, Nullhipotézis elutasítása: {reject_null_right}"

            return (f"Minta átlaga: {sample_mean}\n"
                    f"Z-érték: {z_value}\n\n"
                    f"{left_test_result}\n\n"
                    f"{two_test_result}\n\n"
                    f"{right_test_result}")

    def combobox_selector(self):
        distribution = self.comboBox_2.currentText()
        operation_type = self.comboBox.currentText()
        self.canvas.clear(interval_x=(0,10), interval_y=(0,5))

        m = 0
        s = 0

        text = self.lineEdit_2.toPlainText()
        lines = self.number_of_lines(text)
    
        if operation_type in ["T próba", "U próba"]:
            if operation_type == "T próba":
                if distribution == "Egymintás t próba":
                    if len(lines) == 1:
                        try:
                            x = self.str_to_list(lines[0])
                            mu = int(self.mu.toPlainText())
                            alpha = float(self.sigma.toPlainText())
                        except:
                            self.label_2.setText("Hiányzik valamelyik érték!")
                        else:
                            res = self.t_test(x=x, mu=mu, alpha=alpha)
                            self.label_2.setText(res)
                    else:
                        self.label_2.setText("Egy listát adj meg!")
                elif distribution == "Kétmintás párosított t próba":
                    if len(lines) == 2:
                        try:
                            x = self.str_to_list(lines[0])
                            y = self.str_to_list(lines[1])
                            alpha = float(self.sigma.toPlainText())
                        except:
                            self.label_2.setText("Hiányzik valamelyik érték!")
                        else:
                            res = self.t_test(x=x, y=y, alpha=alpha, paired=True)
                            self.label_2.setText(res)
                    else:
                        self.label_2.setText("Két listát adj meg!")
                elif distribution == "Kétmintás t próba":
                    if len(lines) == 2:
                        try:
                            x = self.str_to_list(lines[0])
                            y = self.str_to_list(lines[1])
                            alpha = float(self.sigma.toPlainText())
                        except:
                            self.label_2.setText("Hiányzik valamelyik érték!")
                        else:
                            res = self.t_test(x=x, y=y, alpha=alpha)
                            self.label_2.setText(res)
                    else:
                        self.label_2.setText("Két listát adj meg!")

            if operation_type == "U próba":
                if distribution == "Egymintás u próba":
                    if len(lines) == 1:
                        try:
                            x = self.str_to_list(lines[0])
                            mu = int(self.mu.toPlainText())
                            alpha = float(self.alpha.toPlainText())
                            sigma = int(self.sigma.toPlainText())
                        except:
                            self.label_2.setText("Hiányzik valamelyik érték!")
                        else:
                            res = self.u_test(X=x, mu=mu, sigma=sigma, alpha=alpha)
                            self.label_2.setText(res)
                    else:
                        self.label_2.setText("Egy listát adj meg!")

        if distribution == "Normál":

            try:
                self.label_2.setText("")

                m = float(self.mu.toPlainText())
                s = float(sqrt(float(self.sigma.toPlainText())))
                X = Normal("X", m, s)
                x = symbols("x")

                if operation_type == "Valószinűség":
                    if self.lineEdit_2.toPlainText() == "":
                        self.label_2.setText("Adjon meg feltételt!")
                    else:
                        condition = sympify(self.lineEdit_2.toPlainText(), locals={"X": X})
                        self.label_2.setText(str(N(P(condition))))

                elif operation_type == "Várható érték":
                    self.label_2.setText(str(E(X)))

                elif operation_type == "Entrópia":
                    try:
                        self.label_2.setText(str(entropy(X)))
                    except:
                        self.label_2.setText("Hiba")
                    else:
                        self.label_2.setText(str(round(entropy(X).evalf(), 4)))

                elif operation_type == "Variancia":
                    self.label_2.setText(str(variance(X)))

                elif operation_type == "Sűrűség függvény":
                    self.label_2.setText(str(density(X)(x)))
                    func_str = self.label_2.text()
                    self.canvas.plot_function(func_str, interval_x=(-5, 5), interval_y=(0,1))
                #
            except:
                self.label_2.setText("ERROR helytelen input!")

        elif distribution == "Geometriai":
            try:
                self.label_2.setText("")
                try:
                    p = float(self.mu.toPlainText())
                except ValueError:
                    self.label_2.setText("ERROR helytelen input!")
                else:
                    if p <= 0.0 or p >= 1.0:
                        self.label_2.setText("A valószínűségnek 0 és 1 között kell lennie")
                    else:
                        X = Geometric("X", p)
                        x = symbols("x")
                        if operation_type == "Valószinűség":
                            if self.lineEdit_2.toPlainText() == "":
                                self.label_2.setText("Adjon meg feltételt!")
                            else:
                                condition = sympify(self.lineEdit_2.toPlainText(), locals={"X": X})
                                self.label_2.setText(str(P(condition)))
                        if operation_type == "Várható érték":
                            self.label_2.setText(str(E(X)))
                        elif operation_type == "Entrópia":
                            self.label_2.setText(str(entropy(X)))
                        elif operation_type == "Variancia":
                            self.label_2.setText(str(variance(X)))
                        elif operation_type == "Sűrűség függvény":
                            self.label_2.setText(str(density(X)(x)))
                            print(str(density(X)(x)))
                            func_str = self.label_2.text()
                            self.canvas.plot_function(func_str, interval_x=(-5, 5), interval_y=(0,1))
            except:
                self.label_2.setText("ERROR helytelen input!")

        elif distribution == "Poisson":
            try:
                self.label_2.setText("")
                λ_value = int(self.mu.toPlainText())
                if λ_value <= 0:
                    self.label_2.setText("Helytelen lambda")
                else:
                    X = Poisson("X", λ_value)
                    x = symbols("x")
                    if operation_type == "Valószinűség":
                        if self.lineEdit_2.toPlainText() == "":
                            self.label_2.setText("Adjon meg feltételt!")
                        else:
                            condition = sympify(self.lineEdit_2.toPlainText(), locals={"X": X})
                            self.label_2.setText(str(N(P(condition))))
                    if operation_type == "Várható érték":
                        self.label_2.setText(str(E(X)))
                    elif operation_type == "Entrópia":
                        self.label_2.setText(str(entropy(X).evalf()))
                    elif operation_type == "Variancia":
                        self.label_2.setText(str(variance(X)))
                    elif operation_type == "Sűrűség függvény":
                        self.label_2.setText(str(density(X)(x)))
                        #JAVÍT vlmi nem jó
                        func_str = self.label_2.text()
                        self.canvas.plot_function(func_str, interval_x=(0, 15), interval_y=(0,1))
            except:
                self.label_2.setTextInteractionFlags("ERROR helytelen poisson!")

        elif distribution == "Logaritmikus":
            self.label_2.setText("")
            try:
                P_s = sympify(self.string_to_S(self.mu.toPlainText()))
                p = float(eval(self.mu.toPlainText()))
                if p <= 0.0 or p >= 1.0:
                    self.label_2.setText("A valószínűségnek 0 és 1 között kell lennie")
                else:
                    X = Logarithmic("X", P_s)
                    x = symbols("x")
                    if operation_type == "Valószinűség":
                        if self.lineEdit_2.toPlainText() == "":
                            self.label_2.setText("Adjon meg feltételt!")
                        else:
                            condition = sympify(self.lineEdit_2.toPlainText(), locals={"X": X})
                            self.label_2.setText(str(P(condition).evalf()))
                    if operation_type == "Várható érték":
                        self.label_2.setText(str(E(X).evalf()))
                    elif operation_type == "Entrópia":
                        self.label_2.setText(str(entropy(X).evalf()))
                    elif operation_type == "Variancia":
                        self.label_2.setText(str(variance(X).evalf()))
                    elif operation_type == "Sűrűség függvény":
                        result = density(X)(x) 
                        #JAVÍT vlmi nem jó
                        self.label_2.setText(str(result))
                        func_str = self.label_2.text()
                        self.canvas.plot_function(func_str, (-15, 15))
            except:
                self.label_2.setText("ERROR helytelen poisson!")

        elif distribution == "Erlang":
            self.label_2.setText("")
            try:
                k = int(self.mu.toPlainText())
                l = float(self.sigma.toPlainText())
                X = Erlang("X", k, l)
                x = symbols("x")

                if operation_type == "Valószinűség":
                    if self.lineEdit_2.text() == "":
                        self.label_2.setText("Adjon meg feltételt!")
                    else:
                        condition = sympify(self.lineEdit_2.toPlainText(), locals={"X": X})
                        self.label_2.setText(str(P(condition)))

                elif operation_type == "Várható érték":
                    self.label_2.setText(str(E(X)))

                elif operation_type == "Entrópia":
                    e = k - log(l) + log(gamma(k)) + (1 - k) * digamma(k)
                    try:
                        self.label_2.setText(str(e.evalf()))
                    except:
                        self.label_2.setText("Hiba")
                    else:
                        self.label_2.setText(str(round(e.evalf(), 4)))

                elif operation_type == "Variancia":
                    self.label_2.setText(str(variance(X)))

                elif operation_type == "Sűrűség függvény":
                    self.label_2.setText(str(density(X)(x)))
                    func_str = self.label_2.text()
                    self.canvas.plot_function(func_str, (0, 15))
            except:
                self.label_2.setText("ERROR helytelen erlang!")

        elif distribution == "Pareto":
            try:
                xm = int(self.mu.toPlainText())
                alpha = int(self.sigma.toPlainText())
                X = Pareto("X", xm, alpha)
                x = symbols("x")

                if operation_type == "Valószinűség":
                    if self.lineEdit_2.toPlainText() == "":
                        self.label_2.setText("Adjon meg feltételt!")
                    else:
                        condition = sympify(self.lineEdit_2.toPlainText(), locals={"X": X})
                        self.label_2.setText(str(N(P(condition))))

                elif operation_type == "Várható érték":
                    self.label_2.setText(str(E(X)))

                elif operation_type == "Entrópia":
                    self.label_2.setText(str(math.log(xm/alpha) + 1/alpha + 1) )

                elif operation_type == "Variancia":
                    self.label_2.setText(str(variance(X)))

                elif operation_type == "Sűrűség függvény":
                    self.label_2.setText(str(density(X)(x)))
                    func_str = self.label_2.text()
                    self.canvas.plot_function(func_str, (xm, 15))
            except:
                self.label_2.setText("ERROR helytelen pareto!")

    def handle_combobox2_change(self):
        distribution = self.comboBox_2.currentText()

        if distribution in ["Geometriai", "Poisson", "Logaritmikus", "Erlang", "Pareto"]:
            self.sigma.hide()
            if distribution == "Geometriai" or distribution == "Logaritmikus":
                self.mu.setPlaceholderText("p")
            elif distribution == "Poisson":
                self.mu.setPlaceholderText("lambda")
            elif distribution == "Erlang":
                self.sigma.show()
                self.mu.setPlaceholderText("k")
                self.sigma.setPlaceholderText("l")
            elif distribution == "Pareto":
                self.sigma.show()
                self.mu.setPlaceholderText("xm")
                self.sigma.setPlaceholderText("alpha")
        else:
            self.sigma.show()
            self.mu.setPlaceholderText("mu")
            self.sigma.setPlaceholderText("sigma")

        if distribution in ["Egymintás t próba", "Kétmintás párosított t próba", "Kétmintás t próba"]:
            self.sigma.setPlaceholderText("alpha")
            if distribution == "Egymintás t próba":
                self.mu.show()
            else:
                self.mu.hide()
        elif distribution in ["Egymintás u próba", "Kétmintás u próba"]:
            self.mu.setPlaceholderText("m")
            self.alpha.show()
        else:
            self.mu.setPlaceholderText("mu")
            self.alpha.hide()

    def handle_combobox_change(self):
        text = self.comboBox.currentText()
        current_distribution = self.comboBox_2.currentText()  # Save the current selection
        eloszlások = ["Normál", "Geometriai", "Poisson", "Logaritmikus", "Erlang", "Pareto"]
        t = ["Egymintás t próba", "Kétmintás párosított t próba", "Kétmintás t próba"]
        u = ["Egymintás u próba"]

        if text == "Sűrűség függvény":
            self.canvas.show()
        else:
            self.canvas.hide()

        if text == "T próba":
            self.label.hide()
            self.comboBox_2.clear()
            self.comboBox_2.addItems(t)
            self.sigma.setPlaceholderText("alpha")
        elif text == "U próba":
            self.label.hide()
            self.mu.show()
            self.comboBox_2.clear()
            self.comboBox_2.addItems(u)
        else:
            self.label.show()
            self.comboBox_2.clear()
            self.comboBox_2.addItems(eloszlások)
            self.sigma.setPlaceholderText("sigma")
        
        # Restore the previous selection
        index = self.comboBox_2.findText(current_distribution)
        if index != -1:
            self.comboBox_2.setCurrentIndex(index)

        self.handle_combobox2_change()  # Ensure the UI updates correctly based on the new selection

    def retranslateUi(self, Ui_Prob_and_Stat):
        _translate = QtCore.QCoreApplication.translate
        Ui_Prob_and_Stat.setWindowTitle(
            _translate("Ui_Prob_and_Stat", "Valószínűségszámitás és statisztika")
        )
        self.comboBox.setItemText(0, _translate("Ui_Prob_and_Stat", "Valószinűség"))
        self.comboBox.setItemText(1, _translate("Ui_Prob_and_Stat", "Várható érték"))
        self.comboBox.setItemText(2, _translate("Ui_Prob_and_Stat", "Entrópia"))
        self.comboBox.setItemText(3, _translate("Ui_Prob_and_Stat", "Variancia"))
        self.comboBox.setItemText(4, _translate("Ui_Prob_and_Stat", "Sűrűség függvény"))
        self.comboBox.setItemText(5, _translate("Ui_Prob_and_Stat", "T próba"))
        self.comboBox.setItemText(6, _translate("Ui_Prob_and_Stat", "U próba"))
        self.label_2.setText(_translate("Ui_Prob_and_Stat", "Eredmény"))
        self.pushButton.setText(_translate("Ui_Prob_and_Stat", "Enter"))
        self.pushButton_2.setText(_translate("Egyenlet", "Vissza"))
        self.comboBox_2.setItemText(0, _translate("Ui_Prob_and_Stat", "Normál"))
        self.comboBox_2.setItemText(1, _translate("Ui_Prob_and_Stat", "Geometriai"))
        self.comboBox_2.setItemText(2, _translate("Ui_Prob_and_Stat", "Poisson"))
        self.comboBox_2.setItemText(3, _translate("Ui_Prob_and_Stat", "Logaritmikus"))
        self.comboBox_2.setItemText(4, _translate("Ui_Prob_and_Stat", "Erlang"))
        self.comboBox_2.setItemText(5, _translate("Ui_Prob_and_Stat", "Pareto"))
        self.label.setText(_translate("Ui_Prob_and_Stat", "Eloszlás:"))
        self.mu.setPlaceholderText(_translate("Ui_Prob_and_Stat", "mu"))
        self.alpha.setPlaceholderText(_translate("Ui_Prob_and_Stat", "alpha"))
        self.sigma.setPlaceholderText(_translate("Ui_Prob_and_Stat", "sigma"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Ui_Prob_and_Stat = QtWidgets.QMainWindow()
    ui = Ui_Prob_and_Stat()
    ui.setupUi(Ui_Prob_and_Stat)
    Ui_Prob_and_Stat.show()
    sys.exit(app.exec_())