import random
from random import choice
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber
from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtGui import QPixmap


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        label = QLabel(self)
        self.pixmap = QPixmap('G:\Настя\GitHub\playing-with-the-multiplication-table\one_cat.png')
        label.setPixmap(self.pixmap)
        self.setCentralWidget(label)
        self.resize(self.pixmap.width(), self.pixmap.height())
        label.setVisible(False)
        label.resize(200, 200)
        label.move(110, 110)

    def initUI(self):
        width = 300
        height = 300
        self.setMaximumSize(width, height)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Game')
        button = QPushButton('Начать игру', self)
        button.resize(button.sizeHint())
        button.move(150 - int(75 / 2), 150 - 12)
        button.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.close()
        a = str(random.randint(1, 10))
        b = str(random.randint(1, 10))
        randnum = random.randint(1, 4)
        self.second_form = SecondForm(self, a, b, randnum, "    Решите уравнение:")
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.x = random.randint(2, 12)
        self.y = random.randint(2, 12)
        multiplication = [self.x, self.y, self.x * self.y]
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.text_our = QLabel(self)
        self.text_o = QLabel(self)
        self.text_our.setText("Вы ответили неверно :_(")
        self.text_our.move(13, 20)
        self.text_o.setText("Попробуйте ещё раз")
        self.text_o.move(13, 35)
        self.text_o.setVisible(False)
        self.text_our.setVisible(False)
        self.data = ''
        finish = []
        self.primers = []
        for i in range(5):
            z = multiplication
            while 1:
                if z[2] not in finish:
                    self.primers.append(['%s * %s = __' % (z[0], z[1]), z[2]])
                    self.primers.append(['%s * __ = %s' % (z[0], z[2]), z[1]])
                    self.primers.append(['__ * %s = %s' % (z[1], z[2]), z[0]])
                    break
                else:
                    z = multiplication
        for i in range(5):
            z = multiplication
            while 1:
                if z[2] not in finish:
                    self.primers.append(['%s : %s = __' % (z[2], z[1]), z[0]])
                    self.primers.append(['%s : __ = %s' % (z[2], z[0]), z[1]])
                    self.primers.append(['__ : %s = %s' % (z[0], z[1]), z[2]])
                    break
                else:
                    z = multiplication
        self.resultat = choice(self.primers)
        self.primer = self.resultat[0]
        self.otvet = self.resultat[1]
        self.statement = QLabel(args[-1], self)
        self.statement.adjustSize()
        self.primer = QLabel(self.primer, self)
        self.primer.move(15, 40 + 40)
        self.ready_button = QPushButton("Готово!", self)
        self.ready_button.move(2 * 110 - 15, 110 + 60 + 80)
        self.ready_button.clicked.connect(self.result)
        self.your_number = QLCDNumber(self)
        self.your_number.move(100, 40 + 40)
        self.first = QPushButton("1", self)
        self.first.move(15, 80 + 80)
        self.first.clicked.connect(self.vvod1)
        self.second = QPushButton("2", self)
        self.second.move(110, 80 + 80)
        self.second.clicked.connect(self.vvod2)
        self.third = QPushButton("3", self)
        self.third.move(2 * 110 - 15, 80 + 80)
        self.third.clicked.connect(self.vvod3)
        self.quatre = QPushButton("4", self)
        self.quatre.move(15, 110 + 80)
        self.quatre.clicked.connect(self.vvod4)
        self.five = QPushButton("5", self)
        self.five.move(110, 110 + 80)
        self.five.clicked.connect(self.vvod5)
        self.six = QPushButton("6", self)
        self.six.move(2 * 110 - 15, 110 + 80)
        self.six.clicked.connect(self.vvod6)
        self.sept = QPushButton("7", self)
        self.sept.move(15, 110 + 30 + 80)
        self.sept.clicked.connect(self.vvod7)
        self.huit = QPushButton("8", self)
        self.huit.move(110, 110 + 30 + 80)
        self.huit.clicked.connect(self.vvod8)
        self.neuf = QPushButton("9", self)
        self.neuf.move(2 * 110 - 15, 110 + 30 + 80)
        self.neuf.clicked.connect(self.vvod9)
        self.zero = QPushButton("0", self)
        self.zero.move(15, 110 + 60 + 80)
        self.zero.clicked.connect(self.vvod0)
        self.effacer = QPushButton("Стереть", self)
        self.effacer.move(110, 110 + 60 + 80)
        self.effacer.clicked.connect(self.clear)
        self.end = QPushButton("Завершить игру", self)
        self.end.move(110 + 80, 10)
        self.end.clicked.connect(self.open_third_form)

    def clear(self):
        self.data = ""
        self.your_number.display(self.data)

    def vvod1(self):
        self.one = '1'
        if len(self.data) < 3:
            self.data += self.one
            self.your_number.display(self.data)

    def vvod2(self):
        self.two = '2'
        if len(self.data) < 3:
            self.data += self.two
            self.your_number.display(self.data)

    def vvod3(self):
        self.trois = '3'
        if len(self.data) < 3:
            self.data += self.trois
            self.your_number.display(self.data)

    def vvod4(self):
        self.four = '4'
        if len(self.data) < 3:
            self.data += self.four
            self.your_number.display(self.data)

    def vvod5(self):
        self.cinq = '5'
        if len(self.data) < 3:
            self.data += self.cinq
            self.your_number.display(self.data)

    def vvod6(self):
        self.sixx = '6'
        if len(self.data) < 3:
            self.data += self.sixx
            self.your_number.display(self.data)

    def vvod7(self):
        self.seven = '7'
        if len(self.data) < 3:
            self.data += self.seven
            self.your_number.display(self.data)

    def vvod8(self):
        self.eight = '8'
        if len(self.data) < 3:
            self.data += self.eight
            self.your_number.display(self.data)

    def vvod9(self):
        self.nine = '9'
        if len(self.data) < 3:
            self.data += self.nine
            self.your_number.display(self.data)

    def vvod0(self):
        self.z = '0'
        if len(self.data) < 3:
            self.data += self.z
            self.your_number.display(self.data)

    def result(self):
        if str(self.data) == str(self.otvet):
            self.game_correct()
        else:
            self.game_incorrect()

    def game_incorrect(self):
        self.data = ""
        self.your_number.display(self.data)
        self.text_o.setVisible(True)
        self.text_our.setVisible(True)

    def game_correct(self):
        self.close()
        a = str(random.randint(1, 10))
        b = str(random.randint(1, 10))
        randnum = random.randint(1, 4)
        self.second_form = SecondForm(self, a, b, randnum, "    Решите уравнение:")
        self.second_form.show()

    def open_third_form(self):
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
