#Вариант 15. В матрице найти минимальный элемент в предпоследней строке.

import random

matrix= [[random.randint(-10, 10) for _ in range(4)] for _ in range(3)]
print('Исходная матрица >> ')
for row in matrix:
    print(*row)

min_element = min(matrix[-2])

print('Минимальный элемент в предпоследней строке матрицы >> ', min_element)
