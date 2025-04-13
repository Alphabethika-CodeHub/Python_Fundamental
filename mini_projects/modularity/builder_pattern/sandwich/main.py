from builder import SandwichBuilder

sandwich_builder = SandwichBuilder()

komposisi_sandwich = (
    sandwich_builder
    .tambah_roti("Roti Gandum")
    .tambah_daging("Daging Wagyu")
    .tambah_keju("Keju Parmesan")
    .tambah_saus("Saus Mustard")
    .tambah_sayur("Sayur Selada")
    .buat_sandwich()
)

komposisi_sandwich.tampilkan_komposisi_sandwich()