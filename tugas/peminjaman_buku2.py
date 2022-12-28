from datetime import datetime

now = datetime.now()
print("=========================================")
print("SELAMAT DATANG DI PROGRAM PEMINJAMAN BUKU")
print("=========================================")
date_time = now.strftime("%m-%d-%Y %H:%M:%S")
nama = []
tanggal = []
kelas = []
nim = []
nama = input("Masukkan Nama anda: ")
kelas= input("Masukkan Kelas anda: ")
nim= int(input("Masukkan Nim anda: "))
print("============================================================================================")
print("                    PEMINJAMAN    BUKU     ONLINE  BINA    SARANA  INFORMATIKA              ")
print("============================================================================================")
print("                             Pilih buku yang ingin anda pinjam                              ")
print("============================================================================================")
print("No       Judul Buku            Penulis       Penerbit")
print("1.Belajar Bahasa Mandari\    Wicaksono Hadi\ Grasindo")
print("2.Belajar Bahasa Pemrograman\Ilana Tan\      Gramedia Pustaka Utama")
print("3.Belajar Bahasa eropa\      Winna Efendi\   Bukunesia")
print("4.Laskar Pelangi\            Andrea Hirata\  Gema Insani")
print("5.Negeri 5 Menara\           Raditya Dika\   Bintang Media")
print("6.Tips menjadi programmer\   Ria Fariana\    Kata Depan")
print("7.Bahasa pemrograman\        Andrea Hirata\  Falcon Publishing")

banyak_jenis = int(input("Berapa banyak buku yang ingin dipinjam : "))
nama_buku = []
jenis_buku = []
nam_buku = []

i= 0
while i<banyak_jenis:
    print("Buku Ke - ", i+1)
    
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
    elif nama_buku[i] == "7" or nama_buku[i] == "Bahasa pemrograman" :
        jenis_buku.append("Bahasa pemrograman")
    else :
        jenis_buku.append("Kode Salah")
    i= i + 1

print("==================================================================")
print("Nama :",nama)
print("Kelas : ",kelas)
print("Nim : ",nim)
print("Tanggal Peminjaman:",date_time)
print("Tanggal pengembalian :Maksimal 2 minggu setelah tanggal peminjaman")
print("==================================================================")
print("No                       Nama buku yang dipinjam")
print("==================================================================")
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


