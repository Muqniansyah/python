# array 3 dimensi
# Membuat array tiga dimensi
array_3d = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

print(array_3d)
# Mengakses elemen array tiga dimensi
print(array_3d[0][1][2])  # Output: 6
print(array_3d[2][0][1])  # Output: 20
print("")

# Mengganti nilai array_3d[0][1][2]
array_3d[0][1][2] = 100

# Mengganti nilai array_3d[2][0][1]
array_3d[2][0][1] = 200

print(array_3d)
print("")
print("")


# Menambahkan data baru ke array
new_data = [[28, 29, 30], [31, 32, 33], [34, 35, 36]]
array_3d.append(new_data)

# Menampilkan array setelah penambahan data
print(array_3d)
print("")
print("")

# Menghapus data pada indeks ke-1 (lapisan kedua)
del array_3d[1]
print(array_3d)