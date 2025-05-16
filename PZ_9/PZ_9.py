# Дана строка апельсины 45 991 63 100 12 яблоки 13 47 26 0 16 отражающая продажи продукции по дням в кг
# Преобразовать информацию из строки в словари
# Найти максимальные продажи по каждому виду продукции
# Результаты вывести на экран

data = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'  # Исходная строка

parts = data.split()  # Разделяем строку на части

sales_data = {}  # Создаем словарь для хранения данных о продажах

current_product = None  # Переменная для хранения текущего продукта

for part in parts:  # Обрабатываем каждую часть
    if part.isalpha():  # Если это слово, то это название продукта
        current_product = part
        sales_data[current_product] = []  # Пустой список для продаж
    else:   # Если это число, добавляем его в соответствующий список продаж
        if current_product is not None:
            sales_data[current_product].append(int(part))

max_sales = {product: max(sales) for product, sales in sales_data.items()}  # Теперь найдём максимальные продажи по каждому виду продукции
   
for product, max_sale in max_sales.items():
    print(f"Максимальные продажи {product}: {max_sale} кг")
