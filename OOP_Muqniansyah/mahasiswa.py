class mahasiswa_ubsi :
    def __init__(self, name, jurusan, ipk):
        self.nama = name
        self.jurusan = jurusan
        self.ipk = ipk
    
    def tampilkan_profil(self):
        print("Nama     : ", self.nama)
        print("Jurusan  : ", self.jurusan)
        print("IPK      : ", self.ipk)
        print()


mahasiswa1 = mahasiswa_ubsi("Mongkey D Luffy","Ilmu Komputer", 3.05)
mahasiswa2 = mahasiswa_ubsi("Nami","Ilmu Komputer", 3.99)
mahasiswa3 = mahasiswa_ubsi("Nico Robin","Ilmu Komputer", 4.00)


mahasiswa1.tampilkan_profil()
mahasiswa2.tampilkan_profil()
mahasiswa3.tampilkan_profil()
