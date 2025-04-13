from mini_projects.modularity.vehicle.kendaraan.kendaraan import Kendaraan


class Mobil(Kendaraan):
    def __init__(self):
        super().__init__("Mobil")

    def bergerak(self):
        print(f"{self.nama} Bergerak!")