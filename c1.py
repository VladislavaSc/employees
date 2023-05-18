import datetime


class Employee:
    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
              # self.__email = f'{self.name.lower()}.{self.surname.lower()}@myjobmail.com'
        self.__pay = pay

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.surname}, {self.pay})'

    def __str__(self):
        return f'{self.fullname} ({self.pay})'

    def __len__(self):
        return len(self.fullname)

    def __add__(self, other):
        return self.pay + other.pay

    def raise_pay(self):
        self.__pay *= self.raise_coef

        @classmethod
        def from_string(cls, data_string):
            name, surname, pay = data_string.split(' ')
            pay = int(pay)

            return cls(name, surname, pay)

        @classmethod
        def set_raise_amount(cls, new_coef):
            cls.raise_coef = new_coef

        @staticmethod
        def is_workday():
            now = datetime.datetime.now()    #.replace(day=16)
            if now.weekday() == 5 or now.weekday() == 6:
                return False
            return True

        @property
        def email(self):
            return f'{self.name.lower()}.{self.surname.lower()}@myjobmail.com'    #  return self.__email

        @property
        def pay(self):
            return self.__pay

        @property
        def fullname(self):
            return f'{self.name} {self.surname}'

        @fullname.setter
        def fullname(self, data_string):
            name, surname = data_string.split(' ')
            self.name = name
            self.surname = surname
            # return f'{self.name} {self.surname}'


if __name__ == '__c1__':
    emp1 = Employee('John', 'Johnson', 60000)
    emp2 = Employee('Jacob', 'Smith', 100000)

    result = emp1 + emp2

    # TestCase#1 Email
    assert emp1.email == 'john.johnson@myjobmail.com'

    # TestCase#1.1 Email
    emp1.name = 'Adam'
    assert emp1.email == 'adam.johnson@myjobmail.com'

    # TestCase#2 RaisePay
    emp1.raise_pay()

    assert 60000 * Employee.raise_coef == emp1.pay

    assert emp1.pay == 90000

    # TestCase #3 New object
    emp2 = Employee.from_string('Jacob Smith 70000')
    assert isinstance(emp2, Employee)
    assert emp2.name == 'Jacob'
    assert emp2.surname == 'Smith'
    assert emp2.pay == 70000

    # TestCase #4 Set raise amount
    Employee.set_raise_amount(2)

    assert Employee.raise_coef == 2
    assert emp1.raise_coef == 2
    assert emp2.raise_coef == 2

    # TestCase#5 Is workday
    Employee.is_workday() == True

    #TestCase#6 Get fullname
    assert emp1.fullname == 'Adam Johnson'
    assert emp2.fullname == 'Jacob Smith'

    #TestCase#7 Set fullname (name, surname)
    emp1.fullname = 'John Johnson'
    assert emp1.name == 'John'
    assert emp1.surname == 'Johnson'

    print(repr(emp1))
    # print(emp1)
    # print(len(emp1))
    print(result)