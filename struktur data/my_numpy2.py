import numpy as np

# Membuat array NumPy
arr = np.array([1, 2, 3, 4, 5])
print("Array asli:", arr)

# Operasi matematika pada array
arr_squared = np.square(arr)
print("Array setelah dipangkatkan 2:", arr_squared)

# Operasi statistik pada array
arr_mean = np.mean(arr)
print("Rata-rata array:", arr_mean)

arr_sum = np.sum(arr)
print("Jumlah semua elemen array:", arr_sum)

# Membentuk array multidimensi
multi_arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array multidimensi:")
print(multi_arr)

# Akses elemen array
print("Elemen pada baris ke-1, kolom ke-2:", multi_arr[1, 2])

# Melakukan operasi pada array multidimensi
row_sum = np.sum(multi_arr, axis=1)
print("Jumlah elemen per baris:", row_sum)

# Menggunakan fungsi bawaan NumPy
random_arr = np.random.rand(3, 3)
print("Array acak:")
print(random_arr)
