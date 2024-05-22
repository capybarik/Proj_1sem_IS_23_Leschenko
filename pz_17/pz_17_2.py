#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 2 – 9.
# ПЗ №2 Вариант 15 Дано трехзначное число. Вывести вначале его последнюю цифру
# (единицы), а затем — его среднюю цифру (десятки)


from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x400')
root.title("Вывод единиц и десятков трехзначного числа")

def close():
    root.destroy()
    root.quit()

def count_num(event):
    num = int(n.get())
    last_digit = num % 10
    middle_digit = (num // 10) % 10
    last.config(text=f"Единицы: {last_digit}")
    middle.config(text=f"Десятки: {middle_digit}")

label = Label(root, text="Введите трехзначное число", font=("Arial", 12), bg="#A188A6")
label.grid(row=1, column=1, columnspan=1, sticky='ew', pady=10)

n = Entry(root, font=("Arial", 12))
n.grid(row=2, column=1, columnspan=1, sticky='ew', pady=10)

button1 = Button(root, text="Обработать", font=("Arial", 12), foreground="#A188A6", background="#1E1E24")
button1.bind("<Button-1>", count_num)
button1.grid(row=3, column=1, columnspan=1, sticky='ew', pady=10)

last = Label(root, font=("Arial", 12, "bold"), foreground="#A188A6")
last.grid(row=4, column=1, columnspan=1, sticky='ew', pady=10)

middle = Label(root, font=("Arial", 12, "bold"), foreground="#A188A6")
middle.grid(row=5, column=1, columnspan=1, sticky='ew', pady=10)

# Настройка ширины колонок
root.grid_columnconfigure(0, weight=1) # Боковые колонки растягиваются
root.grid_columnconfigure(1, weight=0) # Центральная колонка не растягивается
root.grid_columnconfigure(2, weight=1)

root.mainloop()

