from mesin_modern import MesinModern
from mesin_lama import MesinLama

class AdapterMesin(MesinModern):
    def __init__(self, _mesin_lama):
        self._mesin_lama = MesinLama()

    def run(self):
        self._mesin_lama.jalankan()

