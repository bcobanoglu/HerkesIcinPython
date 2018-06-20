#author:Bülent Çobanoğlu
from abc import ABC, abstractmethod
#soyut sınıf:soyutSinif
class soyutSinif(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()
    #soyut metot:islem
    @abstractmethod
    def islem(self):
        pass

class OnEkle(soyutSinif):
    def islem (self):
        return self.value + 10

class OnCarp(soyutSinif):
    def islem(self):
        return self.value * 10
#ana program
x = OnEkle(5)
y = OnCarp(5)
print(x.islem())
print(y.islem())
