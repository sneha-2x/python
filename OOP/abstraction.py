from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,model):
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(f'{self.model} is started')
    def stop(self):
        print(f'{self.model} is stopped')

class Bike(Vehicle):
    def start(self):
        print(f'{self.model} is started')
    def stop(self):
        print(f'{self.model} is stopped')
if __name__ == '__main__':
    car = Car('BMW')
    car.start()
    car.stop()
    bike = Bike('Yamaha')
    bike.start()
    bike.stop()