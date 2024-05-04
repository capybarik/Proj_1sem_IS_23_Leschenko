class User:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_values(self):
        print(f"{self.age = }")
        print(f"{self.name = }")

import pickle

with open("User.bin", "wb") as file:
    pickle.dump(User, file)

with open("User.bin", "rb") as file:
   user = pickle.load(file)

# print(file)

a = User(10, "Max")
a.get_values()