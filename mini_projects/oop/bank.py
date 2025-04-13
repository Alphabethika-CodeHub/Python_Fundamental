class BankAccount:
    def __init__(self, pemilik, saldo = 0):
        self.pemilik = pemilik
        self.__saldo = saldo # Private Attribute (Encapsulation)

    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Deposit berhasil. Saldo Sekarang: {self.__saldo}")
        else:
            print("Jumlah deposit harus positif")

    def withdraw(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan berhasil. Saldo sekarang: {self.__saldo}")
        else:
            print("Saldo tidak mencukupi atau jumlah tidak valid")

    def get_saldo(self):
        return self.__saldo

account = BankAccount("Andi", 500)
print("Saldo: ", account.get_saldo())
account.deposit(1000)
account.withdraw(250)
print("Saldo: ", account.get_saldo())
account.withdraw(5000)
account.deposit(-10)