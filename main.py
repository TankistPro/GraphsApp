#pyuic5 form.ui -o ui.py -x
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
        #Берм диапазон X
        minX = int(self.minX.text())
        maxX = int(self.maxX.text())
        expression = self.lineEdit.text().replace(" ", "")
        if("/0" in expression):
            print("На нолб делить нельзя")
            return
        #Получаем значения X  в указанном диапазоне с шагом
        x = np.arange(minX, maxX + 1, 1)
        y = eval(expression)

        fig, ax = plt.subplots(figsize=(6, 6))

        ax.plot(x, y)
        ax.set(title= f"График функции: { expression }")

        ax = plt.gca()

        #Настройка оси координат
        #Добавление сетки, ее толщина
        ax.grid(axis = 'both', linewidth=1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        #  Устанавливаем интервал основных делений:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
        #  Устанавливаем интервал вспомогательных делений:
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
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