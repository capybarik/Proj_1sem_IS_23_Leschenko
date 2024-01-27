#Вариант 15.  Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
#количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

with open('text18-15.txt', 'r', encoding='utf-16') as file:
    content = file.read()
    print("Содержимое файла >> \n")
    print(content, '\n')
    lowercase = 0
    for char in content:
        if char.islower():
            lowercase += 1

    print("Количество букв в нижнем регистре >> ", lowercase)

    # Замена символов нижнего регистра на верхний и запись в новый файл
    uppercase = content.upper()
    with open('text18-15-uppercase.txt', 'w', encoding='utf-16') as new_file:
        new_file.write(uppercase)



