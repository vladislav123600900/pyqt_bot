from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton 
)
from PyQt6.QtCore import Qt
from random import randint

def start_game():
    button1.hide()
    button2.hide()
    label.setText("Я загадал число от 1 до 100, напиши это число в сторчку")
    answer.show()
    button3.show()
    global win_number
    win_number = randint(0, 100)

def compare():
    user_number = int(answer.text())
    if user_number == win_number:
        label.setText("Победа")
    elif user_number > win_number:

        label.setText(f"Мое число меньше чем {user_number}")
    elif user_number < win_number:
        label.setText(f"Мое число больше чем {user_number}")

app = QApplication([])

WINDOW = QWidget()
WINDOW.resize(200,300)
WINDOW.setWindowTitle("Угадай мое число")
line = QVBoxLayout()
WINDOW.setStyleSheet("background-color: #40F999")


label = QLabel()
label = QLabel("Привет! Сыграем в игру угадай число?")
line.addWidget(label)


button1 = QPushButton("Погнали!")
button1.clicked.connect(start_game)
line.addWidget(button1)

button2 = QPushButton("Не хочу")
button2.clicked.connect(exit)
line.addWidget(button2)

button3 = QPushButton("Проверь число")
button3.clicked.connect(compare)
button3.hide()
line.addWidget(button3)


answer = QLineEdit()
line.addWidget(answer)
answer.hide()

WINDOW.setLayout(line)
WINDOW.show()
app.exec()
    
