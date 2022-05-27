from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox
from PyQt5 import uic
from main import *
from sqllite3_atiri import *
import sqlite3
import sys

a = []

class FirstWind(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('greet.ui', self)
        self.pb.clicked.connect(self.next)

    def next(self):
        self.close()
        self.ch = Choosing()
        self.ch.show()


class Choosing(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('choose.ui', self)
        self.setWindowTitle('Приветствуем Вас!')
        self.pb.clicked.connect(self.next)

    def next(self):
        f1 = open('dict.TXT', 'r+')
        f1.write(self.checkBox.text() + ' ')
        h = self.checkBox.isChecked()
        f1.write(str(h) + '\n')
        f1.write(self.checkBox2.text() + ' ')
        h = self.checkBox2.isChecked()
        f1.write(str(h) + '\n')
        f1.write(self.checkBox3.text() + ' ')
        h = self.checkBox3.isChecked()
        f1.write(str(h) + '\n')
        f1.write(self.checkBox4.text() + ' ')
        h = self.checkBox4.isChecked()
        f1.write(str(h) + '\n')
        f1.write(self.checkBox5.text() + ' ')
        h = self.checkBox5.isChecked()
        f1.write(str(h) + '\n')
        f1.write(self.checkBox6.text() + ' ')
        h = self.checkBox6.isChecked()
        f1.write(str(h) + '\n')
        f1.write(self.checkBox7.text() + ' ')
        h = self.checkBox7.isChecked()
        f1.write(str(h) + '\n')
        f1.close()
        '''themes['IT'][1] = self.checkBox.isChecked()
        themes['python'][1] = self.checkBox2.isChecked()
        themes['c++'][1] = self.checkBox3.isChecked()
        themes['java'][1] = self.checkBox4.isChecked()
        themes['sport'][1] = self.checkBox5.isChecked()
        themes['health'][1] = self.checkBox6.isChecked()
        themes['literature'][1] = self.checkBox7.isChecked()
        print(themes)'''
        self.close()
        self.menu = Menu()
        self.menu.show()


class Greeting(QMainWindow):  # приветственное окно
    def __init__(self):
        super().__init__()
        uic.loadUi('1.1.ui', self)
        self.pb.clicked.connect(self.updating)

    def updating(self):
        self.close()
        self.menu = Menu()
        self.menu.show()


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('2.1.ui', self)
        self.setWindowTitle('Главное меню')
        self.combo = QComboBox(self)
        th = open('dict.TXT', 'r+')
        for line in th:
            c = line.split()
            if c[1] == 'True':
                self.combo.addItem(c[0])
        self.combo.move(370, 200)
        self.pb.clicked.connect(self.page)

    def page(self):
        p = self.combo.currentText()
        a.append(p)
        self.close()
        self.page = Page()
        self.page.show()


class Page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('page.ui', self)
        self.lab = QLabel(self)
        self.lab.setText(fetch())
        self.lab.move(50,50)
        self.linksbrowser = QTextBrowser(self)
        self.linksbrowser.move(50,100)
        self.linksbrowser.setOpenExternalLinks(True)
        link = '<a href="https://stackoverflow.com/questions/49309034">LINK</a>'
        dict = {'smth if we need it': link}
        for key, value in dict.items():
            self.linksbrowser.append('<span>{0}: {1}</span>'.format(key, value))
        self.pb.clicked.connect(self.back)
    def back(self):
        self.close()
        self.menu = Menu()
        self.menu.show()



def start():
    app = QApplication(sys.argv)
    f = open('counter.TXT', 'r+')
    counter = f.read()
    if not counter:
        fw = FirstWind()
        fw.show()
        f.write('opened')
        sys.exit(app.exec_())
    else:
        ex = Greeting()
        ex.show()
        sys.exit(app.exec_())
