class Employee:

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.email = f'{self.name.lower()}.{self.surname.lower()}@myjobmail.com'
        self.pay = pay

if __name__ == '__c1__':
    emp1 = Employee('Ivan', 'Ivanov', 60000)

# TestCase#1 Email
    assert emp1.email == 'Ivan.Ivanov@myjobmail.com'