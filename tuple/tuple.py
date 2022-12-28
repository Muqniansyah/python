# membuat tuple kosong
my_tuple = ()
print(my_tuple)

# tuple dengan 1 elemen
my_tuple = (1,)
print(my_tuple)

# tuple berisi integer
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple bersarang
my_tuple = ("hello", [1, 2, 3], (4, 5, 6))
print(my_tuple)

# tuple bisa tidak menggunakan tanda ()
my_tuple = 1, 2, 3
print(my_tuple)

# memasukkan anggota tuple ke variabel yang bersesuaian 
# a akan berisi 1, b akan berisi 2, dan c akan berisi 3
a, b, c = my_tuple
print(a, b, c)