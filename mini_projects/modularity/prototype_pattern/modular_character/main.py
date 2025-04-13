from karakter import Karakter

# Buat Karakter Original
karakter_original = Karakter("Ragnar", "Kapak Guntur", "Serangan Petir")

# Clone Karakter Untuk Jadi Versi Lain
karakter_clone1 = karakter_original.clone()
karakter_clone1.nama = "Loki"
karakter_clone1.senjata = "Belati Bayangan"
karakter_clone1.skill = "Teleportasi"

karakter_clone2 = karakter_original.clone()
karakter_clone2.nama = "Freya"
karakter_clone2.senjata = "Busur Aurora"
karakter_clone2.skill = "Serangan Panah Cahaya"

# Tampilkan Semua Karakter
karakter_original.tampil()
karakter_clone1.tampil()
karakter_clone2.tampil()

