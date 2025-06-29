# В двумерном списке элементы на главной диагонали увеличить в 2 раза.

try:
    import random

    size = 3
    matrix = [[random.randint(1, 10) for i in range(size)] for i in range(size)]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    result = [
        [elem * 2 if i == j else elem for j, elem in enumerate(row)]
        for i, row in enumerate(matrix)
    ]

    print("\nМатрица после преобразования:")
    for row in result:
        print(row)

except ValueError:
    print("Ошибка")

