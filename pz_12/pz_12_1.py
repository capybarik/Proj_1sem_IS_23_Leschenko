#Вариант 15. В последовательности на n целых чисел найти и вывести:
#1. максимальный среди положительных
#2. минимальный среди отрицательных
#3. произведение элементов


from functools import reduce

numbers = [1, -2, 7, -6, 2, -3]
print('Последовательность целых чисел >> ', numbers)

max_num = 0
min_num = 0
for num in numbers:
    if num > 0 and num > max_num:
        max_num = num
    elif num < 0 and num < min_num:
        min_num = num

print('Максимальное среди положительных >> ', max_num)
print('Минимальное среди отрицательных >> ', min_num)
print('Произведение чисел >> ', reduce(lambda x, y: x * y, numbers))
