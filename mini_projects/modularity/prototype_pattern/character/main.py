import copy


class Karakter:
    def __init__(self, nama, senjata):
        self.nama = nama
        self.senjata = senjata

    def tampil(self):
        print(f"{self.nama} memakai {self.senjata}")

    def clone(self):
        return copy.deepcopy(self)


# Contoh Penggunaan
k1 = Karakter("Lisa", "Long Sword")
k2 = k1.clone()
k2.nama = "Berd"
k2.senjata = "Double Blade"

k1.tampil()
k2.tampil()