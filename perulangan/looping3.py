# contoh penggunaan while
hitung = 0 
while (hitung < 5):
    print("Hitung mulai dari : ", hitung)
    hitung = hitung + 1
print('Good bye!')

# contoh penggunaan while else
# python dukung penggunaan else sebagai pasangan dari while. blok else hanya dieksekusi bila kondisi while bernilai salah.

count = 0 
while (count < 8):
    print(count, 'kurang dari 8')
    count = count + 1
else:
    print(count, 'tidak kurang dari 8')