try:
    a = int(input("Введите целое число a: "))
    if a % 2 == 0:  # проверка условия
        print("Число a является четным")
    else:
        print("Число a не является четным")

except ValueError:
    print("ошибка")
