try:
    a = int(input("Введите целое число a: "))
    if a % 2 == 0:  # проверка условия
        print("True")
    else:
        print("False")

except ValueError:
    print("ошибка")
