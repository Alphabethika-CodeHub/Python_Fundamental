from sandwich import Sandwich

class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def tambah_roti(self, roti):
        self.sandwich.roti = roti
        return self

    def tambah_daging(self, daging):
        self.sandwich.daging = daging
        return self

    def tambah_saus(self, saus):
        self.sandwich.saus = saus
        return self

    def tambah_keju(self, keju):
        self.sandwich.keju = keju
        return self

    def tambah_sayur(self, sayur):
        self.sandwich.sayur = sayur
        return self

    def buat_sandwich(self):
        return self.sandwich