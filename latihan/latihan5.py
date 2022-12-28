print("                       TOKO MAINAN ANAK")
print("                   *************************")

nama_pembeli = input("Masukkan Nama Pembeli : ")
kode_mainan = int(input("Masukkan Kode Mainan : "))
harga = int(input("Masukkan harga :"))
beli = int(input("Masukkan jumlah beli :"))

print("==============================")
print("Nama Pembeli : " + str(nama_pembeli))
print("Kode Kue : " + str(kode_mainan))
print("Harga : " + str(harga))
print("jumlah beli : " + str(beli))
print("Total : " + str(harga * beli))