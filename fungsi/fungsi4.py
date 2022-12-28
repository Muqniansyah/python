# pemanggilan fungsi 
def print_info (nama, usia = 17):
    """Fungsi ini menampilkan info yang dimasukkan"""
    print("Nama :", nama)
    print("Usia :", usia)

# memanggil fungsi Print-info
print_info(usia = 29, nama = "Galih")

# pemanggilan fungsi tidak menediakan argumen usia
print_info(nama = "Muqni")