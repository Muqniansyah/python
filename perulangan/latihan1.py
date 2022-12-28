ulang = 2
for i in range(ulang):
    print("Data ke -" + str(i+1))
    nama = input("Masukkan nim anda : ")
    uts = int(input('Masukkan nilai UTS anda : '))
    uas = int(input('Masukkan nilai UAS anda : '))
    print("NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i " %(nama,uts,uas))
    print("-----------------------------------------------/n")