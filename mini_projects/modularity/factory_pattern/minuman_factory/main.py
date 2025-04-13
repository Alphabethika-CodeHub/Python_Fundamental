from factory_minuman import MinumanFactory

m1 = MinumanFactory.buat_minuman("Teh")
m2 = MinumanFactory.buat_minuman("Kopi")
m3 = MinumanFactory.buat_minuman("Susu")

m1.sajikan()
m2.sajikan()
m3.sajikan()