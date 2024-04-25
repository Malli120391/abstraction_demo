from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres=n
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("Hey I am calling from vehicle class")
#v=Vehicle(2)