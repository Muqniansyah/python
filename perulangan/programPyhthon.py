# program 1
# untuk cetak bilangan genap 1 sampai 10.
for i in range(2,12,2):
    print(i)


# program 2
# menjumlahkan bilangan 1 sampai 10.
jum = 0
for i in range(10):
    i = i + 1
    print(i)
    jum = jum + i
print()
print("Jumlah Bilangan 1 - 10 adalah: ",jum)


# program 3
# menggambar segitiga siku-siku dengan melakukan masukan bilangan bulat.
    #Masukan Bilangan Bulat Ineteger pada variabel n
n = int(input("Masukan Bilangan/karakter : "))
    #Lakukan perulangan nested for untuk menghasilkan pola siku-siku
for i in range(0, n):
    for j in range(0, i + 1):
        print('* ', end='')
    print('')