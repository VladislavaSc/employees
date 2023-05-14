class Employee:

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.email = f'{self.name}.{self.surname}@myjobmail.com'
        self.pay = pay

emp1 = Employee('Ivan', 'Ivanov', 60000)

print(emp1)
print(emp1.name)
print(emp1.surname)
print(emp1.pay)
print(emp1.email)
