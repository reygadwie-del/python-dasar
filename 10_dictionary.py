mahasiswa = {
    "nama": "Dimas",
    "nim": "12345",
    "jurusan": "Teknik Informatika",
    "semester": 3
}

print("Nama:", mahasiswa["nama"])
print("NIM:", mahasiswa.get("nim"))
print("\nSemua data:")
for kunci, nilai in mahasiswa.items():
    print(f"- {kunci}: {nilai}")
