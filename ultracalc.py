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
window.resize(250,500)
window.setWindowTitle("Калькулятор")

line = QVBoxLayout()
window.setStyleSheet("background-color: #40F999")

label = QLabel("Вас приветстввует calculator! Выберете действие")
line.addWidget(label)

def plus():
    import plus 

def minus():
    import minus

def multiply():
    import multiply

def divide():
    import divide
    
button_1 = QPushButton("действие - +")
button_1.clicked.connect(plus)
line.addWidget(button_1)
button_2 = QPushButton("действие - -")
button_2.clicked.connect(minus)
line.addWidget(button_2)
button_3 = QPushButton("действие - *")
button_3.clicked.connect(multiply)
line.addWidget(button_3)
button_4 = QPushButton("действие - /")
button_4.clicked.connect(divide)
line.addWidget(button_4)

window.setLayout(line)
window.show()
app.exec()