# Menulis ke file
with open("catatan.txt", "w", encoding="utf-8") as file:
    file.write("Halo dunia!\n")
    file.write("Belajar Python itu menyenangkan.\n")
    file.write("Sampai jumpa!\n")

# Membaca dari file
print("Isi file catatan.txt:")
with open("catatan.txt", "r", encoding="utf-8") as file:
    isi = file.read()
    print(isi)
