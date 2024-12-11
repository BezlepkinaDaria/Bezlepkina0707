# Дан список размера N (N — четное число).
# Поменять местами его первый элемент со вторым, третий — с четвертым и т. д.

try:
    n = int(input("Введите размер списка: "))
    lst = []  # список

    for i in range(n):
        num = int(input("Введите элемент списка: "))
        lst.append(num)  # добавляет 1 элемент в сущ. список

    for i in range(0, n, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

    print("Измененный список:")
    print(lst)

except ValueError:
    print("Ошибка")
