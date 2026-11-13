class AkunBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo  # Atribut privat
    
    def lihat_saldo(self):
        return f"Saldo {self.pemilik}: Rp {self.__saldo}"
    
    def tarik_saldo(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik Rp {jumlah}")
        else:
            print("Saldo tidak cukup")

akun = AkunBank("Rina", 500000)
print(akun.lihat_saldo())
akun.tarik_saldo(100000)
print(akun.lihat_saldo())
