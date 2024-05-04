file = open("out.bin", "wb")
import pickle

actor1 = ["Alex", "26", 35000]
actor2 = ["Martin", "24", 42000]
actor3 = ["Kevin", "22", 53000]
actor4 = ["Max", "23", 78000]

try:
    file = open("out.bin", "wb")
    try:
        pickle.dump(actor1, file)
        pickle.dump(actor2, file)
        pickle.dump(actor3, file)
        pickle.dump(actor4, file)

    finally:
        file.close()

except FileNotFoundError:
    print("Невозможно открыть файл")

file = open("out.bin", "rb")
b1 = pickle.load(file)
b2 = pickle.load(file)
b3 = pickle.load(file)
b4 = pickle.load(file)

print(b1, b2, b3, b4, sep="\n")