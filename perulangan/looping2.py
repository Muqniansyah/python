# fungsi range() untuk looping / looping bilangan berurut
# fungsi len() untuk mendapat panjang/ jumlah elemen suatu data sekuensial/ urut

mapel = ["MTK", "inggris", "arab"]

for i in range(len(mapel)):
    print("saya suka", mapel[i])

# fungsi list() untuk lgsg menampilkan semua item
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 10, 2)))

# fungsi range() tidak menyimpan semua nilai dalam memori secara langsung. ia hanya mengingat batas bawah, batas atas, dan interval.
print(range(10))
print(range(2, 8))
print(range(2, 20, 2))