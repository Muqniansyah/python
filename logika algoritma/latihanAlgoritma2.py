gajpok = 5000000
produk = int(input("Masukkan Produk yang terjual : "))
hsp = int(input("Masukkan Harga Satuan Produk : "))

hjualProduk = produk*hsp 

if produk > 100:
    bonus = 0.2 * hjualProduk
else :
    bonus = 0.1 * hjualProduk

print("Gaji Salesman : ", + (gajpok+bonus))