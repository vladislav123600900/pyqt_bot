from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QCheckBox, QTextEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import json

with open("feedbacks.json", encoding="utf-8") as file:
    feedbacks = json.load(file)

def input_feedback():
    if check.isChecked():
        name.setText(name_input.text() + ", введите отзыв")
        name_input.hide()
        check.hide()
        feedbacks.show()
        line.addWidget(feedbacks)
        button_next.setText("Отправить")

        
def send_feedback():
    win = QMessageBox()
    win.setWindowTitle("Отзыв")
    win.setWindowIcon(QIcon("cart.png"))
    win.setText("Спасибо за отзыв, до свидания!")
    win.exec()
    start_win()

def start_win():
    write_feedback()
    name.setText("Имя")
    name_input.clear()
    feedbacks.clear()
    name_input.show()
    check.setChecked(False)
    check.show()
    feedbacks.hide()
    button_next.setText("Регистрация")

def next_step():
    if button_next.text() == "Регистрация":
        input_feedback()
    else:
        send_feedback()

def write_feedback():
    if name_input.text() in feedbacks:
        feedbacks[name_input.text()].append(feedbacks.toPlainText())
    else:
        feedbacks[name_input.text()] = [feedbacks.toPlainText()]


app = QApplication([])
window = QWidget()
window.resize(250, 300)
window.setWindowTitle("Авторизация")
window.setWindowIcon(QIcon("cart.png"))
window.setStyleSheet("background-color: #AA67D5; color: white;")

name = QLabel("Имя: ")
name.setStyleSheet("font-size: 24px; font-weight: bold;")
name_input = QLineEdit()
name_input.setStyleSheet("font- size: 18px; font-weight: bold; background-color ; #F33F29A;"
                         "padding: 5px; color: #000; ")
check = QCheckBox("Согласие на обработку данных")
button_next = QPushButton("Регистрация")
button_next.setStyleSheet("font-size: 16px; background-color: #6C0AAB; width: 75px;")

line = QVBoxLayout()
line.addWidget(name, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(name_input, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(check, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button_next)
window.setLayout(line)

feedbacks = QTextEdit()
feedbacks.setStyleSheet("font-size: 18px; font-weight: bold; background-color: #F3F29A;"
                        "padding: 5px; color: #000")
line.addWidget(feedbacks)
feedbacks.hide()

button_next.clicked.connect(next_step)
window.show()
app.exec()

with open("feedbacks.json", "w", encoding="utf-8") as file:
    json.dump(feedbacks, file, ensure_ascii=False)

