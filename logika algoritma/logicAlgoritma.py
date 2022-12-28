print("Ibu pergi kepasar")
print("************************")

uangIbu = int(input("masukkan uang ibu : "))
beratTelur = int(input("berat telur ?"))
hargaTelur_1kg = 26000
transport = 3500 * 2


print("=============OUTPUT============")
print("Sisa Uang : " + str(uangIbu - beratTelur * hargaTelur_1kg - transport))
