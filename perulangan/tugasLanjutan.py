# program tentang lagu anak ayam

def lirik_anak_ayam(n):
    print("Tek kotek kotek kotek, anak ayam turun berkotek")
    for i in range(n, 0, -1):
        print("Anak ayam turunlah", i, "mati satu tinggallah", i-1)
    print("Anak ayam turunlah 1 mati satu tinggallah induknya")

# Input bilangan bulat N
N = int(input("Masukkan bilangan bulat N: "))

# Memastikan N dalam batasan 1 ≤ 𝑁 ≤ 100
if N < 1 or N > 100:
    print("Bilangan N tidak sesuai batasan.")
else:
    # Menampilkan lirik lagu
    lirik_anak_ayam(N)
