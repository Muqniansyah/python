from chef import Chef
# tambahkan argumen Chef pada chef_juna, agar chef_juna mewarisi fungsi yg ada pada class Chef
class chef_juna(Chef):
    def menu_special(self):
        print("chef Membuat Nasi Goreng")

b_juna=chef_juna()
b_juna.makanan_pembuka()
b_juna.makanan_utama()
b_juna.makanan_penutup()