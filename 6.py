import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


print("hello world!")


# Функция для вычисления суммы цифр двузначного числа
def calculate_sum():
    number = int(line_edit.text()) # Получаем введенное пользователем число
    sum_of_digits = number // 10 + number % 10 # Вычисляем сумму цифр
    result_label.setText(f'Сумма цифр: {sum_of_digits}') # Выводим результат на экран

# Функция для определения кратности пяти
def check_divisibility():
    number = int(line_edit.text()) # Получаем введенное пользователем число
    if number % 5 == 0: # Проверяем кратность пяти
        result_label.setText('Кратно пяти: Да') # Выводим результат на экран
    else:
        result_label.setText('Кратно пяти: Нет') # Выводим результат на экран

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Вычисление суммы и кратности')

layout = QVBoxLayout()

label = QLabel('Введите двузначное число:')
layout.addWidget(label)

line_edit = QLineEdit()
layout.addWidget(line_edit)

sum_button = QPushButton('Сумма')
sum_button.clicked.connect(calculate_sum) # При нажатии на кнопку "Сумма" вызываем функцию calculate_sum
layout.addWidget(sum_button)

divisibility_button = QPushButton('Кратность')
divisibility_button.clicked.connect(check_divisibility) # При нажатии на кнопку "Кратность" вызываем функцию check_divisibility
layout.addWidget(divisibility_button)

result_label = QLabel('')
layout.addWidget(result_label)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
