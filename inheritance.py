class Employee:
    raise_coef = 1.04

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef


class Developer(Employee):
    raise_coef = 1.1


class Tester(Employee):
    pass


emp1 = Employee('Adam', 'Miller', 50000)
print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)

dev1 = Developer('John', 'Smith', 100000)
dev2 = Developer('Michel', 'Johnson', 150000)

print(dev1.pay)
dev1.raise_pay()
print(dev1.pay)

print(dev2.pay)
dev2.raise_pay()
print(dev2.pay)