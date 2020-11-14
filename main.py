#pyuic5 form.ui -o ui.py -x
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import numpy as np
import matplotlib.pyplot as plt
from ui import Ui_GraphsApp

class App(QtWidgets.QMainWindow, Ui_GraphsApp):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()
        self.button_clicked()

    def initUI(self):
        #Создание формы и Ui
        self.setupUi(self)
        #Фиксируем размер окна
        self.setFixedSize(self.geometry().width(), self.geometry().height())
        #Показывает наше окно
        self.show()

    def button_clicked(self):
        #Событие клика на кнопку
        self.pushButton.clicked.connect(self.drawGraph)

    def drawGraph(self):
        #x = int(self.spinBox.text())
        expression = self.lineEdit.text()

        x = np.arange(-10, 10, 0.05)
        y = np.arange(-10, 10, 0.05)

        fig, ax = plt.subplots()

        ax.plot(y, eval(expression))
        ax = plt.gca()

        #Настройка оси координат
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        fig.savefig('graph')

        self.changeImage()

    def changeImage(self):
        pixmap = QPixmap("graph.png")
        self.label_5.setPixmap(pixmap)
        
    
#Экземпляр класса QApplication
app = QtWidgets.QApplication(sys.argv)
#Csоздание инстанса App
graphs = App()
#Запуск
sys.exit(app.exec_())