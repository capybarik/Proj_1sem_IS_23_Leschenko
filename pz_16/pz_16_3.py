# Вариант 15
# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.


import pickle
class Bank:
    def __init__(self, sum, percent):
        self.sum = sum
        self.percent = percent

def save_bank(money, filename):
    with open(filename, 'wb') as f:
        pickle.dump(money, f)

def load_bank(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

money1 = Bank(1000, 12)
money2 = Bank(2000, 7)
money3 = Bank(670, 20)

money = [money1, money2, money3]
save_bank(money, 'Bank.bin')

# Загружаем информацию о студентах из файла
loaded_money = load_bank('Bank.bin')

# Выводим информацию о загруженных студентах
for money in loaded_money:
    print(f'Сумма: {money.sum}, Процент: {money.percent}')