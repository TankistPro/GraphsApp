# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphsApp(object):
    def setupUi(self, GraphsApp):
        GraphsApp.setObjectName("GraphsApp")
        GraphsApp.setWindowModality(QtCore.Qt.NonModal)
        GraphsApp.resize(1144, 600)
        GraphsApp.setWindowTitle("Graphs Гусев ПКС-32")
        self.tabWidget = QtWidgets.QTabWidget(GraphsApp)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1151, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 520, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 520, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 500, 441, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 240, 411, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(60, 160, 61, 31))
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(430, 20, 700, 540))
        self.graphicsView.setObjectName("graphicsView")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(438, 29, 681, 521))
        self.label_5.setText("")
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 170, 721, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(GraphsApp)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GraphsApp)

    def retranslateUi(self, GraphsApp):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("GraphsApp", "Построить"))
        self.label.setText(_translate("GraphsApp", "y ="))
        self.label_2.setText(_translate("GraphsApp", "Вы можете сохранить полученный график:"))
        self.pushButton_2.setText(_translate("GraphsApp", "Сохранить график"))
        self.label_3.setText(_translate("GraphsApp", "Обозначения:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("GraphsApp", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("GraphsApp", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("GraphsApp", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("GraphsApp", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("GraphsApp", "Новая строка"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("GraphsApp", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("GraphsApp", "Описание"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("GraphsApp", "+"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("GraphsApp", "Сложение"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("GraphsApp", "-"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("GraphsApp", "Вычитание"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("GraphsApp", "/"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("GraphsApp", "Деление"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("GraphsApp", "x**n"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("GraphsApp", "Возведение X в степень N"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("GraphsApp", "sqrt(x)"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("GraphsApp", "Квадратный корень из X"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("GraphsApp", "x ="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("GraphsApp", "Главная"))
        self.plainTextEdit.setPlainText(_translate("GraphsApp", "Программа предназначен для построения графиков различных функций в двумерных координатах. Просто задайте вид функции и нажмите кнопку \"Построить\". Для эффективного использования всех возможностей сервиса рекомендуется посетить раздел «Главная» => «Обозначения».\n"
"\n"
"Версия программного продука: v1.0.0Beta\n"
"\n"
"\n"
"Выполнил студент группы ПКС-32 Гусев Николай Константинович"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("GraphsApp", "О приложении"))
