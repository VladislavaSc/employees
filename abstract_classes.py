from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):

    def move(self):
        print('car moving')


class Motorcycle(Vehicle):

    def move(self):
        print('moto moving')


car = Car()
moto = Motorcycle()
call = [car, moto]
# car.move()
# moto.move()

for v in call:
    v.move()