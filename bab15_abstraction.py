print('Dila - NIS 123456789')
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, s):
        self.s = s

    def luas(self):
        return self.s ** 2

print("Luas persegi:", Persegi(4).luas())
