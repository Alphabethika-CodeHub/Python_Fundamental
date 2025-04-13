from mini_projects.modularity.vehicle.kendaraan.kendaraan import Kendaraan


class Motor(Kendaraan):
    def __init__(self):
        super().__init__("Motor")

    def bergerak(self):
        print(f"{self.nama} Bergerak!")