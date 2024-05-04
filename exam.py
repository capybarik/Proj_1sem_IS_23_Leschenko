def count_pairs_divisible_by_23(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(i+3, len(seq)):
            if seq[i] * seq[j] % 23 == 0:
                count += 1
    return count

n = int(input("Введите количество чисел: "))
sequence = [int(input()) for _ in range(n)]
result = count_pairs_divisible_by_23(sequence[1:])  # Изменение здесь, sequence[1:] передает подпоследовательность, исключая первый элемент
print(result)