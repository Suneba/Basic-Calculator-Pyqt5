# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import re
#cool

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(303, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 470, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 400, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 160, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 220, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 280, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 160, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 220, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 280, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 160, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 220, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 280, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(100, 340, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 340, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(0, 400, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(100, 470, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(100, 400, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(0, 470, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 301, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(200, 340, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        self.stack = []
        self.integer = []
        self.integer.append(0)
        self.integer.append(0)
        self.operation = ""
        self.decimal = ""

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyCalc"))
        MainWindow.setWindowIcon(QtGui.QIcon("C:/Users/Deepankar/Desktop/py.ico"))
        self.pushButton.setText(_translate("MainWindow", "C"))
        self.pushButton.clicked.connect(lambda: self.clear())

        self.pushButton_2.setText(_translate("MainWindow", "="))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_2.clicked.connect(lambda: self.calculate())

        self.pushButton_3.setText(_translate("MainWindow", "7"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_3.clicked.connect(lambda: self.change(7))

        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_4.clicked.connect(lambda: self.change(4))

        self.pushButton_5.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_5.clicked.connect(lambda: self.change(1))

        self.pushButton_6.setText(_translate("MainWindow", "8"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_6.clicked.connect(lambda: self.change(8))

        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_7.clicked.connect(lambda: self.change(5))

        self.pushButton_8.setText(_translate("MainWindow", "2"))
        self.pushButton_8.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_8.clicked.connect(lambda: self.change(2))

        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_9.clicked.connect(lambda: self.change(9))

        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton_10.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_10.clicked.connect(lambda: self.change(6))

        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_11.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_11.clicked.connect(lambda: self.change(3))

        self.pushButton_12.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_12.clicked.connect(lambda: self.change(0))

        self.pushButton_13.setText(_translate("MainWindow", "."))
        self.pushButton_13.setShortcut(_translate("MainWindow", "."))
        self.pushButton_13.clicked.connect(lambda: self.decimal_call())

        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_14.clicked.connect(lambda: self.operator("+"))

        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_15.clicked.connect(lambda: self.operator("/"))

        self.pushButton_18.setText(_translate("MainWindow", "-"))
        self.pushButton_18.setShortcut(_translate("MainWindow", "-"))
        self.pushButton_18.clicked.connect(lambda: self.operator("-"))

        self.pushButton_19.setText(_translate("MainWindow", "X"))
        self.pushButton_19.setShortcut(_translate("MainWindow", "*"))
        self.pushButton_19.clicked.connect(lambda: self.operator("*"))

        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_16.setText(_translate("MainWindow", "??? "))
        self.pushButton_16.setShortcut(_translate("MainWindow", "Backspace"))
        self.pushButton_16.clicked.connect(lambda: self.delete("deleting"))

    def clear(self):
        print("\nin clear\n________________________________________________")
        self.label.setText("0")
        self.integer[0] = 0
        self.integer[1] = 0
        self.operation = ""
        self.decimal = ""

    def calculate(self):
        print("\nin calculate\n____________________________________________")
        print(bool(self.operation))

        if bool(self.operation) == True:
            if self.op == "+":
                result = self.integer[0] + self.integer[1]
                self.operation = ""
                self.decimal = ""
                self.integer[0] = 0
                self.integer[1] = 0
                self.change(result)

            if self.op == "-":
                result = self.integer[0] - self.integer[1]
                self.operation = ""
                self.decimal = ""
                self.integer[0] = 0
                self.integer[1] = 0
                self.change(result)

            if self.op == "*":
                result = self.integer[0] * self.integer[1]
                if result % 1 == 0:
                    result = int(result)
                    self.operation = ""
                    self.decimal = ""
                    self.integer[0] = 0
                    self.integer[1] = 0
                    self.change(result)
                else:
                    self.operation = ""
                    self.decimal = ""
                    self.integer[0] = 0
                    self.integer[1] = 0
                    self.change(result)

            if self.op == "/":
                result = self.integer[0] / self.integer[1]
                if result % 1 == 0:
                    result = int(result)
                    self.operation = ""
                    self.decimal = ""
                    self.integer[0] = 0
                    self.integer[1] = 0
                    self.change(result)
                else:
                    self.operation = ""
                    self.decimal = ""
                    self.integer[0] = 0
                    self.integer[1] = 0
                    self.change(result)

    def operator(self, op):  # + - * / passed
        self.decimal = ""

        print("\nin operator\n_________________________________")
        self.op = op

        print("\noperation active\n")
        self.operation = "active"

        x = "{}\n{}\n{}".format(self.integer[0], self.op, self.integer[1])
        self.label.setText(x)

    def decimal_call(self):
        print("\nin decimal\n______________________________________________________________")
        selfint1 = re.search('[.]', str(self.integer[1]))
        selfint0 = re.search('[.]', str(self.integer[0]))
        print(bool(selfint0))
        print((selfint1))

        print(".")

        if self.operation == "active":

            if str(bool(selfint1)) == True:
                pass
            else:
                self.decimal = "active"
                print("lol1")
                s = str(self.integer[1])
                int1dot = s + "."
                self.label.setText("{}\n{}\n{}".format(self.integer[0], self.op, int1dot))
        else:
            if str(bool(selfint0)) == True:
                pass
            else:
                self.decimal = "active"
                print("lol0")
                s = str(self.integer[0])
                int0dot = s + "."
                self.label.setText(int0dot)

    def delete(self, delete_command):
        print(delete_command)
        if self.operation == "active":

            self.integer[1] = (self.integer[1] - (self.integer[1] % 10)) // 10
            self.label.setText("{}\n{}\n{}".format(self.integer[0], self.op, self.integer[1]))
        else:
            self.integer[0] = (self.integer[0] - (self.integer[0] % 10)) // 10
            self.label.setText("{}".format(self.integer[0]))

    def change(self, number):
        print("in change\n____________________________________________________________")
        print(number)

        print(bool(self.operation))
        x = bool(self.operation)

        if x == True:

            if self.decimal == "active":

                if bool(re.search("[.]", str(self.integer[1]))) == False:
                    self.stringint1 = str(self.integer[1]) + "." + str(number)
                    print(self.stringint1)
                else:
                    self.stringint1 += str(number)

                self.integer[1] = float(self.stringint1)
                self.label.setText("{}\n{}\n{}".format(self.integer[0], self.op, self.integer[1]))



            else:

                self.integer[1] = (self.integer[1] * 10) + number
                print(number)
                self.label.setText("{}\n{}\n{}".format(self.integer[0], self.op, self.integer[1]))

        else:

            if self.decimal == "active":

                if bool(re.search("[.]", str(self.integer[0]))) == False:

                    self.stringint0 = str(self.integer[0]) + "." + str(number)
                    print(self.stringint0)

                else:
                    self.stringint0 += str(number)

                self.integer[0] = float(self.stringint0)
                self.label.setText(str(float(self.integer[0])))


            else:
                self.integer[0] = (self.integer[0] * 10) + number
                self.label.setText(str(self.integer[0]))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# DELETE IS LATEST #################################################################################################################################
