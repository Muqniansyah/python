sewa = int(input("Masukkan lama sewa : "))

if sewa > 3:
    biaya = (3*6000)+((sewa-3)*5000)
else:
    biaya = sewa*6000

print("Total Biaya : ",biaya)