# tugas kelompok

def gambar_segitiga(N, karakter):
    for i in range(N):
        print((N-i-1) * ' ' + (2*i+1) * karakter)

# Input bilangan bulat N
N = int(input("Masukkan bilangan bulat N: "))

# Memastikan N dalam batasan 1 ≤ 𝑁 ≤ 100
if N < 1 or N > 100:
    print("Bilangan N tidak sesuai batasan.")
else:
    # Input karakter
    karakter = input("Masukkan karakter: ")

    # Menampilkan pola segitiga
    gambar_segitiga(N, karakter)
