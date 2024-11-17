# Составить функцию, которая выполнит суммирования числового ряда

try:  # обработка исключений
    def sum_list(numbers):  # функия
        return sum(numbers)   # возвращение


    my_list = [1, 2, 3, 4, 5]  # числовой ряд
    print(f"Сумма элементов списка: {sum_list(my_list)}")

except ValueError:
    print("Ошибка")
