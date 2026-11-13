from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass
    
    def info(self):
        print("Ini adalah bangun datar.")

class PersegiPanjang(Bentuk):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    
    def luas(self):
        return self.panjang * self.lebar

bentuk = PersegiPanjang(8, 5)
bentuk.info()
print("Luas:", bentuk.luas())
