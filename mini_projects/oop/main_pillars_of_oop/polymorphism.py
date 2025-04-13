from encapsulation import Mobil

# Polymorphism
class Motor:
    def __init__(self, merek):
        self.merek = merek
        self.kecepatan = 0

    def gas(self):
        self.kecepatan += 5
        print(f"{self.merek} digas! Kecepatan sekarang: {self.kecepatan} km/jam")


# Fungsi Yang Menggunakan Polymorphism
def kendaraan_gas(kendaraan):
    kendaraan.gas()

mobil3 = Mobil("Byd", "Merah")
motor = Motor("Ducati")

# Memanggil Fungsi Polymorphism
kendaraan_gas(mobil3)
kendaraan_gas(motor)