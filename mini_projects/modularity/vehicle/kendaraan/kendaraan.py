from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        raise(NotImplementedError("Subclass Harus Mengimplementasikan Method bergerak"))

