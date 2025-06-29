# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое

try:
    import random
    from functools import reduce
    from itertools import chain


    def generate_matrix(rows, cols, min_val=-10, max_val=10):
        return [
            [random.randint(min_val, max_val) for _ in range(cols)]
            for __ in range(rows)
        ]


    def process_matrix(matrix):
        flat_matrix = chain.from_iterable(matrix)

        filtered = filter(lambda x: x > 0 and x % 2 == 0, flat_matrix)
        filtered_list = list(filtered)

        if not filtered_list:
            return filtered_list, 0, 0

        total = reduce(lambda a, b: a + b, filtered_list)

        average = total / len(filtered_list)

        return filtered_list, total, average


    def print_results(matrix, elements, total, avg):
        print("Исходная матрица:")
        for row in matrix:
            print(row)

        print("\nПоложительные четные элементы:", elements)
        print("Сумма элементов:", total)
        print("Среднее арифметическое:", avg)


    def main():
        matrix = generate_matrix(3, 4)

        elements, total, avg = process_matrix(matrix)

        print_results(matrix, elements, total, avg)


    if __name__ == "__main__":
        main()

except ValueError:
    print("Ошибка")