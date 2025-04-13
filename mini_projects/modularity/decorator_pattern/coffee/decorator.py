from minuman import Minuman

class ToppingDecorator(Minuman):
    def __init__(self, minuman):
        self._minuman = minuman

    def buat(self):
        return self._minuman.buat()

class WhippedCream(ToppingDecorator):
    def buat(self):
        return f"{self._minuman.buat()} + Whipped Cream"

class Bubble(ToppingDecorator):
    def buat(self):
        return f"{self._minuman.buat()} + Bubble"

class Caramel(ToppingDecorator):
    def buat(self):
        return f"{self._minuman.buat()} + Caramel"