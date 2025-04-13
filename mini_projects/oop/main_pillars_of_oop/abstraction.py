from abc import ABC, abstractmethod

# Abstraction
class Kendaraan(ABC):
    @abstractmethod
    def klakson(self):
        pass

class Mobil(Kendaraan):
    def klakson(self):
        print(f"Mobil Klakson! Tinn!!")


class Motor(Kendaraan):
    def klakson(self):
        print(f"Motor Klakson! Teettt!!")

mobil = Mobil()
motor = Motor()

mobil.klakson()
motor.klakson()
