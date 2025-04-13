from abc import ABC, abstractmethod

class Minuman(ABC):
    def buat(self):
        pass

class Kopi(Minuman):
    def buat(self):
        return "Kopi"