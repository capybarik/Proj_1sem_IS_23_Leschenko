# Вариант 15
# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег (на год)


class Bank:
    def __init__(self, sum, percent):
        self.sum = sum
        self.percent = percent

    def calculation(self):
        return self.sum * (self.percent/100)

    def withdraw(self):
        return f"Процентные начисления >> {self.calculation()}, вы сможете снять {self.calculation() + self.sum} "

money1 = Bank(1000, 12)
money2 = Bank(2000, 7)
money3 = Bank(670, 20)


print(money1.__dict__)
print(money2.__dict__)
print(money3.__dict__)

print(money1.calculation())
print(money2.calculation())
print(money3.calculation())

print(money1.withdraw())
print(money2.withdraw())
print(money3.withdraw())