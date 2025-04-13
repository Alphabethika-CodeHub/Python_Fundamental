from minuman import Teh, Kopi, Susu

class MinumanFactory:
    @staticmethod
    def buat_minuman(type):
        if type == 'Teh':
            return Teh()
        elif type == 'Kopi':
            return Kopi()
        elif type == 'Susu':
            return Susu()
        else:
            raise ValueError("Tipe Minuman Tidak Dikenali")