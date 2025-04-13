# Encapsulation
class Mobil:
    # Constructor (__init__, method)
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna
        self.kecepatan = 0

    # Method (Fungsi Dalam Class)
    def gas(self):
        self.kecepatan += 10
        print(f"{self.merek} digas! Kecepatan sekarang: {self.kecepatan} km/jam")

    def rem(self):
        self.kecepatan -= 10
        print(f"{self.merek} direm! Kecepatan sekarang: {self.kecepatan} km/jam")

# Membuat Object Baru (Instansiasi)
mobil1 = Mobil("Toyota", "Putih")
mobil2 = Mobil("Jeep", "Hitam")

# Mengakses Attribute
print(mobil1.merek)
print(mobil2.merek)

# Memanggil Method
mobil1.gas()
mobil1.gas()
mobil1.gas()
mobil1.rem()

mobil2.gas()
mobil2.gas()
mobil2.gas()
mobil2.gas()
mobil2.gas()
mobil2.gas()
mobil2.gas()






