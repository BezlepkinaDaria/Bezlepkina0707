# Средствами языка Python сформировать текстовый файл (.txt)
# содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

try:

    def process_numbers(input_file, output_file):
        with open(input_file, 'r') as f:
            numbers = list(map(int, f.read().strip().split()))

        count = len(numbers)
        min_element = min(numbers)
        even_squares = [x ** 2 for x in numbers if x % 2 == 0]
        sum_even_squares = sum(even_squares)
        if even_squares:
            average_even_squares = sum_even_squares / len(even_squares)
        else:
            average_even_squares = 0

        with open(output_file, 'w') as f:
            f.write(f"Исходные данные: {numbers}\n")
            f.write(f"Количество элементов: {count}\n")
            f.write(f"Минимальный элемент: {min_element}\n")
            f.write(f"Квадраты четных элементов: {even_squares}\n")
            f.write(f"Сумма квадратов четных элементов: {sum_even_squares}\n")
            f.write(f"Среднее арифметическое суммы квадратов четных элементов: {average_even_squares}\n")

    process_numbers('input_numbers.txt', 'output_results.txt')

except ValueError:
    print("Ошибка")
