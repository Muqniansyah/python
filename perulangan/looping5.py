# kendali looping break untuk memaksa program keluar dari blok looping ditengah jalan.
for letter in "muqni":
    if letter == "q":
        break
    print("huruf sekarang : ", letter)
print("Good bye!")

# kendali looping continue menyebabkan program lgsg melanjutkan ke step/interval berikutnya, dan mengabaikan (skip) baris kode dibawahnya (yg satu blok). 
for letter in "muqni":
    if letter == "q":
        continue
    print("huruf sekarang : ", letter)
print("Good bye!")