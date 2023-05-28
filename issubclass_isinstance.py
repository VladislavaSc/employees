class Employee:
    raise_coef = 1.04

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef


    def __add__(self, other):
        # if isinstance(other, self.__class__):
            # return self.pay + other.pay
        if issubclass(other.__class__, self.__class__):
            return self.pay + other.pay
        raise Exception


class Developer(Employee):
    raise_coef = 1.1

    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Adam', 'Miller', 50000)

dev1 = Developer('John', 'Smith', 100000, 'python')

total_pay = emp1 + dev1
# total_pay = emp1 + 100000
print(total_pay)
