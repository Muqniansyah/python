# gerobak fried chicken

# Daftar harga ayam
harga_ayam = {
    "D": {"JenisPotong": "Dada", "Harga": 2500},
    "P": {"JenisPotong": "Paha", "Harga": 2000},
    "S": {"JenisPotong": "Sayap", "Harga": 1500}
}

# Input jenis, jenis potong, dan banyak beli
jenis = input("Masukkan jenis ayam (D/P/S): ")
jenis_potong = harga_ayam[jenis]["JenisPotong"]
harga = harga_ayam[jenis]["Harga"]
banyak_beli = int(input("Masukkan jumlah ayam yang dibeli: "))

# Hitung total harga sebelum pajak
total_harga = harga * banyak_beli

# Hitung pajak
pajak = total_harga * 0.1

# Hitung total harga setelah pajak
total_harga_pajak = total_harga + pajak

# Tampilkan tampilan yang diinginkan
print("GEROBAK FRIED CHICKEN")
print("================================")
print("Jenis Potong : ", jenis_potong)
print("Harga        : Rp.", harga)
print("Banyak Beli  : ", banyak_beli)
print("-------------------------------")
print("Total Harga  : Rp.", total_harga)
print("Pajak        : Rp.", pajak)
print("-------------------------------")
print("Total Bayar  : Rp.", total_harga_pajak)
