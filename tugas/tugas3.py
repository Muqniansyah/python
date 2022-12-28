print("\n ^^Form Pendaftaran Kursus^^")
Nama_Siswa = input("Input Nama Siswa : ")
No_Hp = input("Input No. Handphone : ")
Kode_Kursus = input("Masukkan Kode Kursus [PTN/PTS/WPM]")
Biaya_Kursus = int(input("input Biaya Kursus : "))

if (Kode_Kursus=="WPM"):
    diskon = 0.1 * Biaya_Kursus
else:
    diskon = 0 

Total = Biaya_Kursus - diskon



print("\nData Pendaftaran Kursus")
print("=================================")
print("Nama Siswa : " + str(Nama_Siswa))
print("No. Handphone : " + str(No_Hp))
print("Kode Kursus " + str(Kode_Kursus))
print("Biaya Kursus : " + str(Biaya_Kursus))
print("Diskon : " + str(diskon))
print("==================================")
print("Total Biaya : " + str(Total))