#Вариант 15. Составить генератор (yield), который выводит из строки только буквы.

def generator(str):
    for char in str:
        if char.isalpha():
            yield char

str = 'На практическую 12 отводится 4 часа'
letters = generator(str)

for letter in letters:
    print(letter)
