print("=========================================")
print("SELAMAT DATANG DI PROGRAM PEMINJAMAN BUKU")
print("=========================================")
nama = []

kelas = []
nim = []
nama = input("Masukkan Nama anda: ")
kelas= input("Masukkan kelas anda: ")
nim= int(input("masukkan Nim anda: "))

print("===================================================")
print("   PEMINJAMAN BUKU ONLINE BINA SARANA INFORMATIKA  ")
print("===================================================")
print("         Pilih buku yang ingin anda pinjam      ")
print("===================================================")
print("1.Belajar Bahasa Mandarin")
print("2.Belajar bahasa pemrograman")
print("3.Belajar bahasa eropa")
print("4.Laskar Pelangi")
print("5.Negeri 5 Menara")
print("6.Tips Menjadi programmer")
print("7.5 Bahasa pemrograman ter hits")


banyak_jenis = int(input("Berapa banyak buku yang ingin dipinjam : "))
nama_buku = []
jenis_buku = []
nam_buku = []


i= 0
while i<banyak_jenis:
    print("Buku Ke - ", i+1)
    print("1.Belajar Bahasa Mandarin")
    print("2.Belajar bahasa pemrograman")
    print("3.Belajar bahasa eropa")
    print("4.Laskar Pelangi")
    print("5.Negeri 5 Menara")
    print("6.Tips Menjadi programmer")
    print("7.5 Bahasa pemrograman ter hits")
    



    nama_buku.append(input("Masukkan judul buku : "))

    if nama_buku[i] == "1" or nama_buku[i] == "Belajar Bahasa Mandarin" :
        jenis_buku.append("Belajar Bahasa Mandarin")
    elif nama_buku[i] == "2" or nama_buku[i] == "Belajar bahasa pemrograman" :
        jenis_buku.append("Belajar bahasa pemrograman")
    elif nama_buku[i] == "3" or nama_buku[i] == "Belajar bahasa eropa" :
        jenis_buku.append("Belajar bahasa eropa")
    elif nama_buku[i] == "4" or nama_buku[i] == "Laskar pelangi" :
        jenis_buku.append("Laskar pelangi")
    elif nama_buku[i] == "5" or nama_buku[i] == "Negeri 5 Menara" :
        jenis_buku.append("Negeri 5 Menara")
    elif nama_buku[i] == "6" or nama_buku[i] == "Tips menjadi programmer" :
        jenis_buku.append("Tips menjadi programmer")
    elif nama_buku[i] == "7" or nama_buku[i] == "5 Bahasa pemrograman ter hits" :
        jenis_buku.append("5 Bahasa pemrograman ter hits")


    else :
        jenis_buku.append("Kode Salah")
    i= i + 1



print("============================================================")
print("Nama :",nama)
print("Kelas : ",kelas)
print("Nim : ",nim)
print("============================================================")
print("No                       Nama buku yang dipinjam")
print("============================================================")
a = 0
while a < banyak_jenis:
    print('%i                            %s ' % (a+1,jenis_buku[a]))
    a = a + 1

pildex = input("Apakah ada index yang ingin dihapus [y/n] : ")
if pildex == "y":
    banyak_indexs = int(input("Berapa banyak buku yang ingin dihapus: "))
    i = 0
    while i < banyak_indexs:
        print("Index  Ke - ", i+1)
        index = input ("Masukkan index yang ingin dihapus : ")
        print("Index Ke -",index,"Telah dihapus")
        i = i + 1
    print("TERIMAKASIH TELAH MELAKUKAN PEMINJAMAN JAGA BUKU SEBAIK-BAIKNYA")


elif pildex == "n":
    print("TERIMAKASIH TELAH MELAKUKAN PEMINJAMAN JAGA BUKU SEBAIK-BAIKNYA")


else :
    print("Kode Yang dimasukkan Salah")


print("============================================================")
print("Nama :",nama)
print("Kelas : ",kelas)
print("Nim : ",nim)
print("============================================================")
print("No                       Nama buku yang dipinjam")
print("============================================================")
a=0
while a < banyak_jenis:
    print('%i                            %s ' % (a+1,jenis_buku[a]))
    a = a + 1