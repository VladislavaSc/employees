from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        super().__init__()()


class Mixinlog:
    ID = 0

    def __init__(self, name, surname, pay):
        super().__init__(name, surname, pay)
        Mixinlog.ID += 1
        print(f'Added employee number: {self.ID}')


class Developer(Mixinlog, Employee):

    def __init__(self, name, surname, pay, prog_lang):
        print('Developer added')
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang

dev = Developer('Sam', 'Smith', 100000, 'python')
dev = Developer('Sam', 'Smith', 100000, 'python')
dev = Developer('Sam', 'Smith', 100000, 'python')
print(dev.__dict__)
print(Developer.__mro__)