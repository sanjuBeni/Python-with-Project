from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def v_break(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car Started")

    def v_break(self):
        print("Break implement")

    def stop(self):
        print("Cat stop")
    
c = Car()
c.start()
c.v_break()
c.stop()