#Fungsi Pangkat secara Rekursif
def faktorial(a):
    if a == 1:
        return (a)
    else:
        return (a*faktorial(a-1))
bil = int(input("Masukan Bilangan :"))

print("%d! = %d" % (bil,faktorial(bil)))

# cara hitung faktorial
# 6!=6x5!
# 5!=5x4!
# 4!=4x3!
# 3!=3x2!
# 2!=2x1!
# 1!=1x0!
# 6! = 6x5x4x3x2x1 = 720

