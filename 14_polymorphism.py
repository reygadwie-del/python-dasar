class Sepeda:
    def bergerak(self):
        print("Sepeda dikayuh.")

class Mobil:
    def bergerak(self):
        print("Mobil melaju di jalan.")

def mulai_bergerak(kendaraan):
    kendaraan.bergerak()

sepeda = Sepeda()
mobil = Mobil()

mulai_bergerak(sepeda)
mulai_bergerak(mobil)
