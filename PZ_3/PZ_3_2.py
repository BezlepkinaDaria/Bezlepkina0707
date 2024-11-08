#покупка < 500 cкидка 2%
#покупка < 1000 скидка 3%
#покупка < 1500 скидка 4%
#покупка < 2000 скидка 5%
#составить программу, определяющую процентной ставки в зависимости от вносимой суммы

try:
    purchase = float(input("Введите сумму покупки: "))

    discount = 0 #скидка

    if purchase < 500:
        discount = purchase * 0.02 #скидка 2%
    elif purchase < 1000:
        discount = purchase * 0.03 #скидка 3%
    elif purchase < 1500:
        discount = purchase * 0.04 #скидка 4%
    elif purchase < 2000:
        discount = purchase * 0.05 #скидка 5%

    print("Размер скидки составит:", discount)
except ValueError:
    print("Ошибка")
