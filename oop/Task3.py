class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def total_person():
        return f"Количество созданных экземпляров >> {Person.count}"

person1 = Person("Ольга")
person2 = Person("Юлия")
person3 = Person("Анастасия")
person4 = Person("Евсей")
person5 = Person("Илья")
person6 = Person("Витя")

print(Person.total_person())
