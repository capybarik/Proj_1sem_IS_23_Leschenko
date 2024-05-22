# Вариант 15
# Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,
# AN-1, A3, AN-2, ….


A = [1, 2, 3, 4, 5]
N = len(A)  # Определяем размер списка

print(A)
for i in range(N // 2):  # Итерируемся по половине элементов списка
    print(A[i], A[N - 1 - i], end=' ')  # Выводим пары элементов в нужном порядке

if N % 2 != 0:  # Если количество элементов в списке нечетное
    print(A[N // 2])  # Выводим центральный элемент

