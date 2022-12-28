# menampilkan deret bilangan dengan looping for
data = int(input('banyak data : '))

for i in range(data):
    print(i)

# menampilkan deret bilangan genap dengan looping while
nilai = int(input('masukkan nilai : '))
x = 2

while x <= nilai:
    print(x, end=" ")
    x=x+2