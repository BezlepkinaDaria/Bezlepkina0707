# В двумерном списке элементы на главной диагонали увеличить в 2 раза.

try:
    import random
    from functools import partial
    from itertools import starmap


    def generate_matrix(size, min_val=1, max_val=10):
        return [
            [random.randint(min_val, max_val) for _ in range(size)]
            for __ in range(size)
        ]


    def process_row(row_index, row):
        return [
            elem * 2 if j == row_index else elem
            for j, elem in enumerate(row)
        ]


    def main():
        matrix_size = 4

        matrix = generate_matrix(matrix_size)
        print("Сгенерированная матрица:")
        for row in matrix:
            print(row)

        processed_matrix = list(
            starmap(
                process_row,
                enumerate(matrix)
            )
        )

        print("\nМатрица после удвоения главной диагонали:")
        for row in processed_matrix:
            print(row)


    if __name__ == "__main__":
        main()

except ValueError:
    print("Ошибка")

