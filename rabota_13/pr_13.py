from functools import reduce
from operator import mul

# ========== Вариант 1 ==========
def variant1_task1():
    """Перенести внутренние элементы матрицы"""
    Matt2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    Matt1 = [row[1:-1] for row in Matt2[1:-1]]
    print("1. Внутренние элементы:", Matt1)

def variant1_task2():
    """Отрицательные элементы возвести в квадрат"""
    matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    result = [[x**2 if x < 0 else x for x in row] for row in matrix]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 2 ==========
def variant2_task1():
    """Найти минимальный и максимальный элементы"""
    matrix = [[3, 7, 2], [9, 5, 1], [4, 6, 8]]
    flat = [x for row in matrix for x in row]
    print(f"1. Min: {min(flat)}, Max: {max(flat)}")

def variant2_task2():
    """Сумма отрицательных в первой трети матрицы"""
    matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]
    first_third = matrix[:len(matrix)//3 + 1]
    sum_neg = sum(x for row in first_third for x in row if x < 0)
    print(f"2. Сумма: {sum_neg}")

# ========== Вариант 3 ==========
def variant3_task1():
    """Увеличить главную диагональ в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x*2 if i == j else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant3_task2():
    """Сумма и среднее положительных четных элементов"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    positives = [x for row in matrix for x in row if x > 0 and x % 2 == 0]
    sum_p = sum(positives)
    avg = sum_p / len(positives) if positives else 0
    print(f"2. Сумма: {sum_p}, Среднее: {avg}")

# ========== Вариант 4 ==========
def variant4_task1():
    """Увеличить неглавные диагональные элементы в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x*2 if i != j else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant4_task2():
    """Проверить наличие положительных элементов"""
    matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    has_pos = any(any(x > 0 for x in row) for row in matrix)
    print(f"2. {has_pos}")

# ========== Вариант 5 ==========
def variant5_task1():
    """Элементы второго столбца возвести в квадрат"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x**2 if j == 1 else x for j, x in enumerate(row)] for row in matrix]
    print("1. Результат:")
    for row in result:
        print(row)

def variant5_task2():
    """Заменить нечетные элементы на 0"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[0 if x % 2 else x for x in row] for row in matrix]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 6 ==========
def variant6_task1():
    """Элементы первого столбца возвести в куб"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x**3 if j == 0 else x for j, x in enumerate(row)] for row in matrix]
    print("1. Результат:")
    for row in result:
        print(row)

def variant6_task2():
    """Заменить элементы >10 на 0"""
    matrix = [[9, 10, 11], [12, 5, 6], [7, 13, 9]]
    result = [[0 if x > 10 else x for x in row] for row in matrix]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 7 ==========
def variant7_task1():
    """Увеличить строку N на 3"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    result = [[x + 3 if i == N else x for x in row] for i, row in enumerate(matrix)]
    print(f"1. Строка {N} увеличена:")
    for row in result:
        print(row)

def variant7_task2():
    """Заменить последний столбец на -1"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[-1 if j == len(row)-1 else x for j, x in enumerate(row)] for row in matrix]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 8 ==========
def variant8_task1():
    """Увеличить столбец N в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    result = [[x*2 if j == N else x for j, x in enumerate(row)] for row in matrix]
    print(f"1. Столбец {N} увеличен:")
    for row in result:
        print(row)

def variant8_task2():
    """Заменить последнюю строку на 0"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[0 if i == len(matrix)-1 else x for x in row] for i, row in enumerate(matrix)]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 9 ==========
def variant9_task1():
    """Заменить второй столбец элементами массива"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = [10, 11, 12]
    result = [row[:1] + [arr[i]] + row[2:] for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant9_task2():
    """Среднее положительных элементов, кратных 3"""
    matrix = [[3, 6, 9], [2, 5, 8], [12, 7, 4]]
    positives = [x for row in matrix for x in row if x > 0 and x % 3 == 0]
    avg = sum(positives) / len(positives) if positives else 0
    print(f"2. Среднее: {avg}")

# ========== Вариант 10 ==========
def variant10_task1():
    """Заменить третью строку элементами массива"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = [10, 11, 12]
    result = [row if i != 2 else arr for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant10_task2():
    """Среднее положительных элементов"""
    matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    positives = [x for row in matrix for x in row if x > 0]
    avg = sum(positives) / len(positives) if positives else 0
    print(f"2. Среднее: {avg}")

# ========== Вариант 11 ==========
def variant11_task1():
    """Сумма и произведение строки N"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    row = matrix[N]
    row_sum = sum(row)
    row_prod = reduce(mul, row, 1)
    print(f"1. Строка {N}: Сумма: {row_sum}, Произведение: {row_prod}")

def variant11_task2():
    """Сумма второй половины матрицы"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    half = len(matrix) // 2
    total = sum(x for row in matrix[half:] for x in row)
    print(f"2. Сумма: {total}")

# ========== Вариант 12 ==========
def variant12_task1():
    """Сумма и произведение столбца N"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    col = [row[N] for row in matrix]
    col_sum = sum(col)
    col_prod = reduce(mul, col, 1)
    print(f"1. Столбец {N}: Сумма: {col_sum}, Произведение: {col_prod}")

def variant12_task2():
    """Новый массив из отрицательных элементов"""
    matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    negatives = [x for row in matrix for x in row if x < 0]
    print(f"2. Отрицательные: {negatives}, Размер: {len(negatives)}")

# ========== Вариант 13 ==========
def variant13_task1():
    """Среднее нечетных строк"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    averages = [sum(row)/len(row) for i, row in enumerate(matrix) if i % 2 == 0]
    print(f"1. Средние: {averages}")

def variant13_task2():
    """Максимальный положительный кратный 4"""
    matrix = [[3, 8, 12], [16, 5, 20], [4, 24, 8]]
    multiples = [x for row in matrix for x in row if x > 0 and x % 4 == 0]
    max_val = max(multiples) if multiples else None
    print(f"2. Максимальный: {max_val}")

# ========== Вариант 14 ==========
def variant14_task1():
    """Сумма четных столбцов"""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0])) if i % 2 == 1]
    print(f"1. Суммы: {sums}")

def variant14_task2():
    """Минимальный в предпоследнем столбце"""
    matrix = [[3, 7, 2, 5], [9, 5, 1, 8], [4, 6, 8, 3]]
    min_val = min(row[-2] for row in matrix)
    print(f"2. Минимальный: {min_val}")

# ========== Вариант 15 ==========
def variant15_task1():
    """Суммы столбцов и замена второй строки"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    col_sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
    result = [col_sums if i == 1 else row for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant15_task2():
    """Минимальный в предпоследней строке"""
    matrix = [[3, 7, 2], [9, 5, 1], [4, 6, 8], [10, 12, 11]]
    min_val = min(matrix[-2])
    print(f"2. Минимальный: {min_val}")

# ========== Вариант 16 ==========
def variant16_task1():
    """Суммы строк и замена третьего столбца"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_sums = [sum(row) for row in matrix]
    result = [row[:2] + [row_sums[i]] for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant16_task2():
    """Сумма второй половины матрицы"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    half = len(matrix) // 2
    total = sum(x for row in matrix[half:] for x in row)
    print(f"2. Сумма: {total}")

# ========== Вариант 17 ==========
def variant17_task1():
    """Генерация матрицы с преобразованием"""
    start = 1
    step = 2
    size = 3
    matrix = [[start + step*(i*size + j) for j in range(size)] for i in range(size)]
    print("1. Матрица:")
    for row in matrix:
        print(row)

def variant17_task2():
    """Сумма первых двух строк"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    total = sum(x for row in matrix[:2] for x in row)
    print(f"2. Сумма: {total}")

# ========== Вариант 18 ==========
def variant18_task1():
    """Увеличить кратные 3 в 3 раза"""
    matrix = [[1, 3, 5], [6, 8, 9], [12, 7, 4]]
    result = [[x*3 if x % 3 == 0 else x for x in row] for row in matrix]
    print("1. Результат:")
    for row in result:
        print(row)

def variant18_task2():
    """Среднее последних двух столбцов"""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    last_two = [x for row in matrix for x in row[-2:]]
    avg = sum(last_two) / len(last_two)
    print(f"2. Среднее: {avg}")

# ========== Вариант 19 ==========
def variant19_task1():
    """Среднее последних двух столбцов"""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    last_two = [x for row in matrix for x in row[-2:]]
    avg = sum(last_two) / len(last_two)
    print(f"1. Среднее: {avg}")

def variant19_task2():
    """Перенести внутренние элементы матрицы"""
    Matr2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    Matr1 = [row[1:-1] for row in Matr2[1:-1]]
    print("2. Внутренние элементы:", Matr1)

# ========== Вариант 20 ==========
def variant20_task1():
    """Сумма первых двух строк"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    total = sum(x for row in matrix[:2] for x in row)
    print(f"1. Сумма: {total}")

def variant20_task2():
    """Найти минимальный и максимальный элементы"""
    matrix = [[3, 7, 2], [9, 5, 1], [4, 6, 8]]
    flat = [x for row in matrix for x in row]
    print(f"2. Min: {min(flat)}, Max: {max(flat)}")

# ========== Вариант 21 ==========
def variant21_task1():
    """Минимальный в предпоследней строке"""
    matrix = [[3, 7, 2], [9, 5, 1], [4, 6, 8], [10, 12, 11]]
    min_val = min(matrix[-2])
    print(f"1. Минимальный: {min_val}")

def variant21_task2():
    """Увеличить главную диагональ в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x*2 if i == j else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 22 ==========
def variant22_task1():
    """Минимальный в предпоследнем столбце"""
    matrix = [[3, 7, 2, 5], [9, 5, 1, 8], [4, 6, 8, 3]]
    min_val = min(row[-2] for row in matrix)
    print(f"1. Минимальный: {min_val}")

def variant22_task2():
    """Среднее нечетных строк"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    averages = [sum(row)/len(row) for i, row in enumerate(matrix) if i % 2 == 0]
    print(f"2. Средние: {averages}")

# ========== Вариант 23 ==========
def variant23_task1():
    """Максимальный положительный кратный 4"""
    matrix = [[3, 8, 12], [16, 5, 20], [4, 24, 8]]
    multiples = [x for row in matrix for x in row if x > 0 and x % 4 == 0]
    max_val = max(multiples) if multiples else None
    print(f"1. Максимальный: {max_val}")

def variant23_task2():
    """Увеличить неглавные диагональные элементы в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x*2 if i != j else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 24 ==========
def variant24_task1():
    """Новый массив из отрицательных элементов"""
    matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    negatives = [x for row in matrix for x in row if x < 0]
    print(f"1. Отрицательные: {negatives}, Размер: {len(negatives)}")

def variant24_task2():
    """Среднее нечетных строк"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    averages = [sum(row)/len(row) for i, row in enumerate(matrix) if i % 2 == 0]
    print(f"2. Средние: {averages}")

# ========== Вариант 25 ==========
def variant25_task1():
    """Сумма второй половины матрицы"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    half = len(matrix) // 2
    total = sum(x for row in matrix[half:] for x in row)
    print(f"1. Сумма: {total}")

def variant25_task2():
    """Элементы второго столбца возвести в квадрат"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x**2 if j == 1 else x for j, x in enumerate(row)] for row in matrix]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 26 ==========
def variant26_task1():
    """Среднее положительных элементов"""
    matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    positives = [x for row in matrix for x in row if x > 0]
    avg = sum(positives) / len(positives) if positives else 0
    print(f"1. Среднее: {avg}")

def variant26_task2():
    """Элементы первого столбца возвести в куб"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x**3 if j == 0 else x for j, x in enumerate(row)] for row in matrix]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 27 ==========
def variant27_task1():
    """Среднее положительных кратных 3"""
    matrix = [[3, 6, 9], [2, 5, 8], [12, 7, 4]]
    positives = [x for row in matrix for x in row if x > 0 and x % 3 == 0]
    avg = sum(positives) / len(positives) if positives else 0
    print(f"1. Среднее: {avg}")

def variant27_task2():
    """Увеличить строку N на 3"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    result = [[x + 3 if i == N else x for x in row] for i, row in enumerate(matrix)]
    print(f"2. Строка {N} увеличена:")
    for row in result:
        print(row)

# ========== Вариант 28 ==========
def variant28_task1():
    """Заменить последнюю строку на 0"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[0 if i == len(matrix)-1 else x for x in row] for i, row in enumerate(matrix)]
    print("1. Результат:")
    for row in result:
        print(row)

def variant28_task2():
    """Увеличить столбец N в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    result = [[x*2 if j == N else x for j, x in enumerate(row)] for row in matrix]
    print(f"2. Столбец {N} увеличен:")
    for row in result:
        print(row)

# ========== Вариант 29 ==========
def variant29_task1():
    """Заменить последний столбец на -1"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[-1 if j == len(row)-1 else x for j, x in enumerate(row)] for row in matrix]
    print("1. Результат:")
    for row in result:
        print(row)

def variant29_task2():
    """Заменить третью строку элементами массива"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = [10, 11, 12]
    result = [row if i != 2 else arr for i, row in enumerate(matrix)]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 30 ==========
def variant30_task1():
    """Заменить элементы >10 на 0"""
    matrix = [[9, 10, 11], [12, 5, 6], [7, 13, 9]]
    result = [[0 if x > 10 else x for x in row] for row in matrix]
    print("1. Результат:")
    for row in result:
        print(row)

def variant30_task2():
    """Увеличить неглавные диагональные элементы в 2 раза"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[x*2 if i != j else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 31 ==========
def variant31_task1():
    """Заменить нечетные элементы на 0"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[0 if x % 2 else x for x in row] for row in matrix]
    print("1. Результат:")
    for row in result:
        print(row)

def variant31_task2():
    """Заменить второй столбец элементами массива"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = [10, 11, 12]
    result = [row[:1] + [arr[i]] + row[2:] for i, row in enumerate(matrix)]
    print("2. Результат:")
    for row in result:
        print(row)

# ========== Вариант 32 ==========
def variant32_task1():
    """Проверить наличие положительных элементов"""
    matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    has_pos = any(any(x > 0 for x in row) for row in matrix)
    print(f"1. {has_pos}")

def variant32_task2():
    """Сумма и произведение строки N"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    row = matrix[N]
    row_sum = sum(row)
    row_prod = reduce(mul, row, 1)
    print(f"2. Строка {N}: Сумма: {row_sum}, Произведение: {row_prod}")

# ========== Вариант 33 ==========
def variant33_task1():
    """Сумма и среднее положительных четных элементов"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    positives = [x for row in matrix for x in row if x > 0 and x % 2 == 0]
    sum_p = sum(positives)
    avg = sum_p / len(positives) if positives else 0
    print(f"1. Сумма: {sum_p}, Среднее: {avg}")

def variant33_task2():
    """Сумма и произведение столбца N"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1  # Пример ввода
    col = [row[N] for row in matrix]
    col_sum = sum(col)
    col_prod = reduce(mul, col, 1)
    print(f"2. Столбец {N}: Сумма: {col_sum}, Произведение: {col_prod}")

# Выполнение всех вариантов
if __name__ == "__main__":
    # Вызов нужных функций для демонстрации
    variant1_task1()
    variant1_task2()
    # variant2_task1()
    # variant2_task2()
    # ... и так далее для всех нужных вариантов