import random
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QMainWindow, QLabel


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Game')
        button = QPushButton('Начать игру', self)
        button.resize(button.sizeHint())
        button.move(150-int(75/2), 150-12)
        button.clicked.connect(self.open_second_form)

    def open_second_form(self):
        a = str(random.randint(1, 10))
        b = str(random.randint(1, 10))
        randnum = random.randint(1, 4)
        self.second_form = SecondForm(self, a, b, randnum, "Решите уравнение:")
        self.second_form.show()


class Math:
    def __init__(self):
        pass


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        if args[3] == 1:
            sign = "-"
            answer_int = int(args[1]) - int(args[2])
        elif args[3] == 2:
            sign = "+"
            answer_int = int(args[1]) + int(args[2])
        elif args[3] == 3:
            sign = "*"
            answer_int = int(args[1]) * int(args[2])
        else:
            sign = "/"
            answer_int = int(args[1]) / int(args[2])
        statement = QLabel(args[-1], self)
        statement.adjustSize()
        num1 = QLabel(args[1], self)
        num1.move(150, 150)
        num2 = QLabel(args[2], self)
        num2.move(170, 150)
        sign = QLabel(sign, self)
        sign.move(160, 150)
        equals = QLabel("=", self)
        equals.move(180, 150)
        answer = QLabel(str("{:.2f}".format(answer_int)), self)
        answer.move(190, 150)
        ready_button = QPushButton("Готов!", self)
        ready_button.move(150, 200)
        # if ready_button.clicked():
        #     self.game_correct()
        # else:
        #     self.game_incorrect()
        #
        # def game_correct():
        #     pass
        #
        # def game_incorrect():
        #     pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())