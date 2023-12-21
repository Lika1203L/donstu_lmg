# donstu_lmg
bnh bjhb jhvjhv
def calculate_sum():
    number = int(line_edit.text()) # Получаем введенное пользователем число
    sum_of_digits = number // 10 + number % 10 # Вычисляем сумму цифр
    result_label.setText(f'Сумма цифр: {sum_of_digits}') # Выводим результат на экран
def check_divisibility():
    number = int(line_edit.text()) # Получаем введенное пользователем число
    if number % 5 == 0: # Проверяем кратность пяти
        result_label.setText('Кратно пяти: Да') # Выводим результат на экран
    else:
        result_label.setText('Кратно пяти: Нет') # Выводим результат на экран
