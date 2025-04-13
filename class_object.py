import math
from abc import ABC, abstractmethod

# __ini__ Init Merupakan Constructor

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} with color of {self.color} started!")

my_car = Car("Toyota", "Yellow")
# my_car.start()
# print(my_car)

# Challenge Create a Class
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def deskripsi(self):
        print(f"Buku '{self.judul}' ditulis oleh {self.penulis}.")

my_buku = Buku("Atomic Habits", "James Clear")
# my_buku.deskripsi()


# Inheritance
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def suara(self):
        print("Meow")

class Kucing(Hewan):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def main(self):
        print(f"{self.nama} sedang bermain bola.")

my_kucing = Kucing("Kitty", "Angora")
# my_kucing.suara()
# my_kucing.main()

# Encapsulation Example
class BankAccount:
    def __init__(self, nama, saldo):
        self.nama = nama        # Attribute Public
        self.__saldo = saldo    # Attribute Private (Ini Encapsulationnya)

    def lihat_saldo(self):
        print(f"Saldo {self.nama}: Rp{self.__saldo}")

    def tarik_tunai(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil tarik tunai Rp{jumlah}. Sisa saldo: Rp{self.__saldo}")

account = BankAccount("Dapa", 5000000)
# account.lihat_saldo()
# account.tarik_tunai(6000000)
# account.tarik_tunai(1500000)

# Attribute Private Bisa Diakses Dengan Teknik "Name Mangling"
# print("Name Mangling Technique: ", account._BankAccount__saldo)

# Challenge Encapsulation
class Mahasiswa:
    def __init__(self, nama, ipk):
        self.nama = nama
        self.__ipk = ipk

    def lihat_ipk(self):
        print(self.__ipk)

    def set_ipk(self, ipk):
        if 0.0 <= ipk <= 4.0:
            self.__ipk = ipk
            print("OK")
        else:
            print("Gagal")

mhs1 = Mahasiswa("Dapa", 3.0)
# mhs1.set_ipk(5.0)
# mhs1.set_ipk(4.0)
# mhs1.set_ipk(1.7)
# mhs1.lihat_ipk()


# Polymorphism
# class Bentuk:
#     def __init__(self, x):
#         self.x = x
#
#     def luas(self):
#         print(math.pi * self.x * self.x)
#
# class Lingkaran(Bentuk):
#     def __init__(self, x):
#         super().__init__(x)
#
#     def luas(self):
#         print(math.pi * self.x * self.x)
#
# class Persegi(Bentuk):
#     def __init__(self, x):
#         super().__init__(x)
#
#     def luas(self):
#         print(self.x * self.x)
#
# b1 = Lingkaran(7)
# b2 = Persegi(8)
#
# b1.luas()
# b2.luas()

# Refactored Polymorphism
# class Bentuk:
#     def __init__(self, x):
#         self.x = x
#
#     def luas(self):
#         raise(NotImplementedError("Subclass Harus Mengimplementasikan Method Luas"))
#
# class Lingkaran(Bentuk):
#     def luas(self):
#         print(f"Luas Lingkaran: {math.pi * self.x ** 2:.2f}")
#
# class Persegi(Bentuk):
#     def luas(self):
#         print(f"Luas Persegi: {self.x ** 2}")
#
# b1 = Lingkaran(7)
# b2 = Persegi(8)
# b1.luas()
# b2.luas()


# Abstraction
class Bentuk(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def luas(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        super().__init__("Lingkaran")
        self.jari_jari = jari_jari

    def luas(self):
        import math
        return math.pi * self.jari_jari ** 2

class Persegi(Bentuk):
    def __init__(self, sisi):
        super().__init__("Persegi")
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

b1 = Lingkaran(7)
b2 = Persegi(8)
print(b1.luas())
print(b2.luas())

# Challenge
class Kendaraan(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def bergerak(self):
        pass

class Mobil(Kendaraan):
    def __init__(self):
        super().__init__("Mobil")

    def bergerak(self):
        print(f"Mobil Ini Bergerak!")

class Motor(Kendaraan):
    def __init__(self):
        super().__init__("Motor")

    def bergerak(self):
        print(f"Motor Ini Bergerak!")

m1 = Mobil()
m2 = Motor()
m1.bergerak()
m2.bergerak()