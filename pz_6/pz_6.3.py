# Вариант 15
# Дан список размера N. Осуществить циклический сдвиг элементов списка влево на
# одну позицию (при этом AN перейдет в AN-1, AN-1 — в AN-2, . . ., A1 — в AN)

arr = [1, 2, 3, 4, 5]
print(arr)

temp = arr[0]
for i in range(len(arr) - 1):
    arr[i] = arr[i+1]
arr[(len(arr) - 1)] = temp
print(arr)
