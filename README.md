# donstu_lmg
bnh bjhb jhvjhv
def calculate_sum():
    number = int(line_edit.text()) # Получаем введенное пользователем число
    sum_of_digits = number // 10 + number % 10 # Вычисляем сумму цифр
    result_label.setText(f'Сумма цифр: {sum_of_digits}') # Выводим результат на экран
