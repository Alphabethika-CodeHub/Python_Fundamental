from encapsulation import Mobil

# Inheritance
class MobilSport(Mobil):
    def __init__(self, merek, warna, turbo):
        super().__init__(merek, warna)
        self.turbo = turbo

    def aktifkan_turbo(self):
        if self.turbo:
            self.kecepatan += 30
            print(f"Turbo diaktifkan! Kecepatan sekarang: {self.kecepatan} km/jam")
        else:
            print("Mobil ini tidak memiliki turbo")

    # Overriding Method
    def gas(self):
        super().gas() # Memanggil Method Gas Dari Parent Class
        if self.turbo:
            self.kecepatan += 5


mobil_sport = MobilSport("Porsche", "Merah", True)
print(mobil_sport.merek)
mobil_sport.gas()
mobil_sport.aktifkan_turbo()
