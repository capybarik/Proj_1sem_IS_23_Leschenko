# Вариант 15.В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.

import random

matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(3)]
print(' Исходная матрица >> ')
for row in matrix:
    print(*row)

column_sum = []

for j in range(4):
    columns = sum(row[j] for row in matrix)
    column_sum.append(columns)

matrix[1] = column_sum

print(' Преобразованная матрица >> ')
for row in matrix:
    print(*row)
