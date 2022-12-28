print("PROGRAM HITUNG GAJI KARYAWAN")
print("************************")

# input
Namkar = input("Masukkan Nama : ")
Goljab = input("Masukkan Golongan Jabatan [1/2/3] : ")
Pendik = input("Masukkan Pendidikan [SMA/D1/D3/S1] : ")
Jamker = int(input("Masukkan Jam kerja : "))

# proses

Gajpok = 300000 

    # Tunjangan  Jabatan
if Goljab == "1" :
    persentase = 0.5 * Gajpok
elif Goljab == "2" :
    persentase = 0.10 * Gajpok
elif Goljab == "3" :
    persentase = 0.15 * Gajpok
else :
    "Anda Salah Memasukkan Golongan"

    # Tunjangan Pendidikan
if Pendik == "SMA" :
    persentase2 = 0.025 * Gajpok
elif Pendik == "D1" :
    persentase2 = 0.5 * Gajpok
elif Pendik == "D3" :
    persentase2 = 0.20 * Gajpok
elif Pendik == "S1" :
    persentase2 = 0.30 * Gajpok
else :
    "Anda Salah Memasukkan Pendidikan"

    # Honor Lembur
if Jamker >= 8 :
    # lembur = 1 / 173 * Gajpok
    lembur = Gajpok * 3500
elif Jamker > 8 :
    lembur = Gajpok * (3500*2)
else :
    "Anda Salah Memasukkan Jam Kerja" 


# cetak hasil / output
print("-------------------------------")
print("Karyawan yang bernama : " + str(Namkar))
print("Honor yang diterima : " + str(Gajpok))
print("Tunjangan Jabatan :  RP" ,persentase)
print("Tunjangan Pendidikan : RP" ,persentase2)
print("Honor Lembur : RP", lembur)
print("Total Gaji : RP", +(Gajpok+ (persentase+persentase2) + lembur))