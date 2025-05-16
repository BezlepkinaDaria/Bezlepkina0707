# Организовать и вывести последовательность из N случайных целых чисел.
# Из исходной последовательности организовать первую последовательность,
# содержащую числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.
try:
    import random

    def generate_sequences(N):
        original_sequence = [random.randint(1, 100) for _ in range(N)]

        multiples_of_three = [num for num in original_sequence if num % 3 == 0]

        others = [num for num in original_sequence if num % 3 != 0]

        count_multiples_of_three = len(multiples_of_three)
        count_others = len(others)

        return original_sequence, multiples_of_three, others, count_multiples_of_three, count_others

    N = 10
    original, multiples_of_three, others, count_m3, count_others = generate_sequences(N)

    print("Исходная последовательность:", original)
    print("Кратные 3:", multiples_of_three)
    print("Остальные:", others)
    print("Количество кратных 3:", count_m3)
    print("Количество остальных:", count_others)

except ValueError:
    print("Ошибка")