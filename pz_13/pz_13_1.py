# Вариант 15.В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.

import random

matrix= [[random.randint(-10, 10) for _ in range(4)] for _ in range(3)]
print(' Исходная матрица >> ')
for row in matrix:
    print(*row)

column_sum = []
# Вычисляем суммы элементов каждого столбца
for j in range(len(matrix[0])):
    columns = sum(row[j] for row in matrix)  # Суммируем элементы в j-том столбце
    column_sum.append(columns)

# Заменяем элементы второй строки исходной матрицы на полученные суммы
matrix[1] = column_sum

print(' Преобразованная матрица >> ')
for row in matrix:
    print(*row)