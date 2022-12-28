print("Untuk mendapatkan Nilai Terbesar")
print("===================================")

a = 60
b = 20
c = 100
d = 40

if a > b:
    if a > c :
        if a > d :
            print("cetak a")
        else:
            print("cetak d")
    else:
        if c > d :
            print("cetak c")
        else:
            print("cetak d")               
else:
    if b > c :
        if b > d :
            print("cetak b")
        else:
            print("cetak d")
    else:
        if c > d : 
            print("cetak c")
        else: 
            print("cetak d")


