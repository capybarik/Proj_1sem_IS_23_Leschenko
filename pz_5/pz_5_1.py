# Вариант 15
# Составить функцию, которая выведет на экран строку,
# содержащую задаваемое с клавиатуры число символов

def symbols():
    try:
        count = int(input("Введите число символов >> "))
        string = "a" * count
        print(string)
    except ValueError:
        print('Неверный тип данных')
symbols()
