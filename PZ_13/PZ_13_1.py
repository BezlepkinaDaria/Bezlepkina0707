# В двумерном списке элементы на главной диагонали увеличить в 2 раза.

try:
    def double_diagonal(matrix):
        for i in range(min(len(matrix), len(matrix[0]))):
            matrix[i][i] *= 2
        return matrix


    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    updated_matrix = double_diagonal(matrix)

    print("Обновленная матрица:")
    for row in updated_matrix:
        print(row)

except ValueError:
    print("Ошибка")

