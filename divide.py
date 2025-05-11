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

app = QApplication([])

window = QWidget()
window.resize(300,400)
window.setWindowTitle("действие /")

line = QVBoxLayout()
window.setStyleSheet("background-color: #40F999")

label = QLabel("Впишите 1 и 2 число в 2 строчки")
line.addWidget(label)

def compare():
    answer = QLineEdit()

number1 = QLineEdit()
number2 = QLineEdit()
answer = QLineEdit()

def divide():
    summ = int(number1.text()) / int(number2.text())
    answer.setText(f"Ответ: {summ}")
    answer.show()
    

button1 = QPushButton("Разделить")
button1.clicked.connect(divide)
line.addWidget(button1)

line.addWidget(number1)
line.addWidget(number2)

answer = QLabel()
line.addWidget(answer)
answer.hide()


window.setLayout(line)
window.show()
app.exec()