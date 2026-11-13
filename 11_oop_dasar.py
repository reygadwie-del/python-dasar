class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara.")

kucing = Hewan("Si Belang", "Kucing")
kucing.bersuara()
