import os

#вывод текущей директории
#print("Текущая директория: ", os.getcwd())

#создание пустого каталога
#os.mkdir("folder")

#проверка на наличие уже такой папки
#if not os.path.isdir("folder"):
    #os.mkdir("folder")

#изменение текущего каталога на фолдер
#os.chdir("folder")
#print("Текущая директория изменилась на  фолдер:", os.getcwd())

#создание вложенных папок

#os.makedirs("nested1/nested2/nested3")

#создание нового текстового файла
text_file = open("text.txt", "w")
text_file.write("Это текстовый файл")
text_file.close()

#переименование файла
#os.rename("text.txt","renamed-text.txt")

#перемещение файлов
#os.replace("renamed-text.txt", "folder/renamed-text.txt")

#все папки
#print("Все папки и файлы: ", os.listdir())

#for dirpath, dirnames, filenames in os.walk("."):
    #for dirname in dirnames:
        #print("Каталог: ", os.path.join(dirpath,dirname))
   # for filename in filenames:
        #print("Файл:", os.path.join(dirpath, filename))

#удаление файлов
#os.remove("folder/renamed-text.txt")

#удаление папки
#os.rmdir("folder")

#удаление вложенных папок
#os.removedirs("nested1/nested2/nested3")

#получение информации о файлах
print("Размер файла:",os.stat("text.txt").st_size)
