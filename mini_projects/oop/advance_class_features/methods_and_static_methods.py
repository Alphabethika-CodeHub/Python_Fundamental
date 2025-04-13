import math


class Pizza:
    def __init__(self, bahan):
        self.bahan = bahan

    def __str__(self):
        return f"Pizza Dengan {self.bahan}"

    @classmethod
    def margherita(cls):
        return cls(["keju", "tomat"])

    @classmethod
    def pepperoni(cls):
        return cls(["pepperoni", "keju", "tomat"])

    @staticmethod
    def ukuran_luas(jari_jari):
        return math.pi * jari_jari ** 2


p1 = Pizza.margherita()
p2 = Pizza.pepperoni()
print(p1)
print(p2)

print(Pizza.ukuran_luas(12))