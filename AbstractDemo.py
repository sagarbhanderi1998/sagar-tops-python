from abc import ABC,abstractmethod

class Vehical(ABC):

    @abstractmethod
    def tyre(self):
        pass
    def speed(self):
        print("Drive Your Vehical With Limited Speed")

class Bike(Vehical):

    def __init__(self):
        print("Bike's Object Created")
    def __del__(self):
        print("Bike's Object Deleted")
    def speed(self):
        super().speed()
        print("Bike's Max Speed Is 120")
    def tyre(self):
        print("I have 2 tyres")

class Car(Vehical):

    def speed(self):
        print("Car's Max Speed Is 160")
    def tyre(self):
        print("I have 4 tyres")

b1=Bike()
b1.tyre()
b1.speed()
del b1
c1=Car()
c1.tyre()
c1.speed()
