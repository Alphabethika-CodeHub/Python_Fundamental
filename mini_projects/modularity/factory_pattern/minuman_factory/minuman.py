from abc import ABC, abstractmethod

class Minuman(ABC):
    @abstractmethod
    def sajikan(self):
        pass

class Teh(Minuman):
    def sajikan(self):
        print("Teh Disajikan")

class Susu(Minuman):
    def sajikan(self):
        print("Susu Disajikan")

class Kopi(Minuman):
    def sajikan(self):
        print("Kopi Disajikan")