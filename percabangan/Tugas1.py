print("Pendaftaran Mahasiswa Baru")
print("=============================")

# input
Nis = int(input("Masukkan NIS Anda : "))
Nama = input("Masukkan Nama Anda : ")
Jurusan = input("Masukkan Jurusan anda [SI/SIA] : ")

# proses
if Jurusan == "SI":
    Nama_Prodi = "Sistem Informasi"
    harga = 2400000
else: 
    Nama_Prodi = "Sistem Informasi akuntansi"
    harga = 2000000

# cetak hasil
print("-------------------------------------")
print("Pendaftaran Mahasiswa Baru")
print("Nis : " + str(Nis))
print("Nama : " + str(Nama))
print("Jurusan : " + str(Jurusan))
print("Nama Prodi : " + str(Nama_Prodi))
print("Harga : ", + (harga))







