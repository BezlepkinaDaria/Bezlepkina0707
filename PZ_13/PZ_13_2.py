# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое

try:
    import random

    rows, cols = 3, 4
    matrix = [[random.randint(-10, 10) for i in range(cols)] for i in range(rows)]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    # Фильтрация положительных четных элементов
    positive_even = [elem for row in matrix for elem in row if elem > 0 and elem % 2 == 0]

    # Вычисление суммы и среднего значения
    total = sum(positive_even) if positive_even else 0
    average = total / len(positive_even) if positive_even else 0

    print("\nПоложительные четные элементы:", positive_even)
    print("Сумма элементов:", total)
    print("Среднее арифметическое:", average)

except ValueError:
    print("Ошибка")