import copy


class Karakter:
    def __init__(self, nama, senjata, skill):
        self.nama = nama
        self.senjata = senjata
        self.skill = skill

    def tampil(self):
        print(f"""
Karakter: {self.nama}
Senjata: {self.senjata}
Skill: {self.skill}
        """)

    def clone(self):
        return copy.deepcopy(self)