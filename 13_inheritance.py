class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def perkenalan(self):
        print(f"Nama saya {self.nama}, umur {self.umur} tahun.")

class Mahasiswa(Orang):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)
        self.jurusan = jurusan
    
    def perkenalan(self):
        super().perkenalan()
        print(f"Saya belajar di jurusan {self.jurusan}")

mhs = Mahasiswa("Farhan", 21, "Sistem Informasi")
mhs.perkenalan()
