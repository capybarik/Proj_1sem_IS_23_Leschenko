#На вход программы поступает последовательность из N целых положительных чисел, все числа в последовательности различны.
#Рассматриваются все пары различных элементов последовательности, находящихся на расстоянии не меньше чем 3
#(разница в индексах элементов пары должна быть 3 или более, порядок элементов в паре неважен).
#Необходимо определить количество таких пар, для которых произведение элементов делится на 23.
def count_pairs(seq):
    count = 0
    for i in range(n):
        for j in range(i+3, n):
            if seq[i] * seq[j] % 23 == 0:
                count += 1
    return count

n = int(input())
sequence = [int(input()) for _ in range(n)]
result = count_pairs(sequence)
print(result)
