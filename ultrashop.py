import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Онлайн-магазин")
    window.setGeometry(200, 100, 500, 600)

    layout = QVBoxLayout()

    title = QLabel(" Онлайн-магазин")
    title.setFont(QFont("Arial", 18))
    layout.addWidget(title)

    products = [
        {"name": "Футболка", "price": 1200},
        {"name": "Кроссовки", "price": 3500},
        {"name": "Джинсы", "price": 2700},
        {"name": "Куртка", "price": 5200},
    ]

    cart = []
    total = 0

    cart_list = QListWidget()
    total_label = QLabel("Итого: 0₽")
    total_label.setFont(QFont("Arial", 14))

    def add_to_cart(product):
        nonlocal total
        cart.append(product)
        item = QListWidgetItem(f"{product['name']} - {product['price']}₽")
        cart_list.addItem(item)
        total += product['price']
        total_label.setText(f"Итого: {total}₽")

    for product in products:
        row = QHBoxLayout()
        name = QLabel(f"{product['name']} — {product['price']}₽")
        btn = QPushButton("Добавить в корзину")
        btn.clicked.connect(lambda checked, p=product: add_to_cart(p))
        row.addWidget(name)
        row.addWidget(btn)
        layout.addLayout(row)


    layout.addWidget(QLabel("\n🧺 Ваша корзина:"))
    layout.addWidget(cart_list)
    layout.addWidget(total_label)

    def place_order():
        nonlocal total
        if not cart:
            QMessageBox.warning(window, "Корзина пуста", "Добавьте товары перед оформлением заказа.")
            return
        QMessageBox.information(window, "Спасибо за заказ", f"Вы оформили заказ на сумму {total}₽!")
        cart.clear()
        cart_list.clear()
        total = 0
        total_label.setText("Итого: 0₽")

    order_btn = QPushButton("Оформить заказ")
    order_btn.setStyleSheet("background-color: green; color: white; font-size: 14px;")
    order_btn.clicked.connect(place_order)
    layout.addWidget(order_btn)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()