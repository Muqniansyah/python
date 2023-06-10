print("PROGRAM HITUNG GAJI KARYAWAN")
print("************************")

# input
Namkar = input("Masukkan Nama : ")
golongan = int(input("Masukkan golongan karyawan (1/2/3): "))
tingkat_pendidikan = input("Masukkan tingkat pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# Gaji pokok
gaji_pokok = 300000

# Tunjangan jabatan
persentase_tunjangan_jabatan = 0
if golongan == 1:
    persentase_tunjangan_jabatan = 0.05
elif golongan == 2:
    persentase_tunjangan_jabatan = 0.1
elif golongan == 3:
    persentase_tunjangan_jabatan = 0.15
else :
    "Anda Salah Memasukkan Golongan"

tunjangan_jabatan = persentase_tunjangan_jabatan * gaji_pokok

# Tunjangan pendidikan
persentase_tunjangan_pendidikan = 0
if tingkat_pendidikan == "SMA":
    persentase_tunjangan_pendidikan = 0.025
elif tingkat_pendidikan == "D1":
    persentase_tunjangan_pendidikan = 0.05
elif tingkat_pendidikan == "D3":
    persentase_tunjangan_pendidikan = 0.2
elif tingkat_pendidikan == "S1":
    persentase_tunjangan_pendidikan = 0.3
else :
    "Anda Salah Memasukkan Pendidikan"

tunjangan_pendidikan = persentase_tunjangan_pendidikan * gaji_pokok

# Honor lembur
jam_normal = 8
honor_lembur = 0
if jam_kerja > jam_normal:
    kelebihan_jam = jam_kerja - jam_normal
    honor_lembur = kelebihan_jam * 3500
else :
    "Anda Salah Memasukkan Jam Kerja" 

# Total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Tampilkan hasil /OUTPUT
print("PT. DINGIN DAMAI")
print("===============================")
print("Karyawan yang bernama : " + str(Namkar))
print("Honor yang diterima        : Rp.", gaji_pokok)
print("Tunjangan Jabatan  : Rp.", tunjangan_jabatan)
print("Tunjangan Pendidikan: Rp.", tunjangan_pendidikan)
print("Honor Lembur       : Rp.", honor_lembur)
print("-------------------------------")
print("Total Gaji         : Rp.", total_gaji)
