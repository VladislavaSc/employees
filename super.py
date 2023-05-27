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

    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Adam', 'Miller', 50000)
print(emp1.__dict__)

dev1 = Developer('John', 'Smith', 100000, 'python')

print(dev1.__dict__)
