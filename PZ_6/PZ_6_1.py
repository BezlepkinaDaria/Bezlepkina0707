# Дан первый член A и разность D арифметической прогрессии.
# Сформировать и вывести список размера 10, содержащий 10 первых членов данной прогрессии:
# A, A + D, A + 2*D, A + 3*D, ... .

try:
    A = 2
    D = 3
    progression = []

    for i in range(10):
        progression.append(A + i * D)  # добавляет элемент в конец списка

    print(progression)

except ValueError:
    print("Ошибка")
