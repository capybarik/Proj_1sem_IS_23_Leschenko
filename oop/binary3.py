import pickle

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

def save_students(students, filename):
    with open(filename, 'wb') as f:
        pickle.dump(students, f)

def load_students(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Создаем несколько объектов студентов
student1 = Student('Алексей', 20, 4.2)
student2 = Student('Мария', 19, 3.8)
student3 = Student('Иван', 21, 4.5)

# Сохраняем информацию о студентах в файл
students = [student1, student2, student3]
save_students(students, 'students.bin')

# Загружаем информацию о студентах из файла
loaded_students = load_students('students.bin')

# Выводим информацию о загруженных студентах
for student in loaded_students:
    print(f'Имя: {student.name}, Возраст: {student.age}, Средний балл: {student.gpa}')