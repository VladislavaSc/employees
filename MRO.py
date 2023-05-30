from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay


class Mixinlog:
    ID = 0

    def __init__(self):
        print(f'Added employee number: {self.ID}')

class Developer(Employee, Mixinlog):

    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang

dev = Developer('Sam', 'Smith', 100000, 'python')
print(dev.__dict__)