from mesin_lama import MesinLama
from adapter import AdapterMesin

mesin_lama = MesinLama()
mesin_modern = AdapterMesin(MesinLama)

mesin_modern.run()