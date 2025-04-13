class Sandwich:
    def __init__(self):
        self.roti = None
        self.daging = None
        self.saus = None
        self.sayur = None
        self.keju = None

    def tampilkan_komposisi_sandwich(self):
        print(f"""
Komposisi Sandwich Terdiri Dari:
 - {self.roti}
 - {self.daging}
 - {self.saus}
 - {self.sayur}
 - {self.keju}            
        """)