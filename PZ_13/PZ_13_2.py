# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое

try:
    def positive_even_stats(matrix):
        positive_evens = []

        for row in matrix:
            for num in row:
                if num > 0 and num % 2 == 0:
                    positive_evens.append(num)

        total_sum = sum(positive_evens)
        average = total_sum / len(positive_evens) if positive_evens else 0

        return positive_evens, total_sum, average


    matrix = [
        [1, -2, 3],
        [4, 6, -8],
        [7, 8, 10]
    ]

    positives, total_sum, average = positive_even_stats(matrix)

    print("Положительные четные элементы:", positives)
    print("Сумма положительных четных элементов:", total_sum)
    print("Среднее арифметическое:", average)

except ValueError:
    print("Ошибка")