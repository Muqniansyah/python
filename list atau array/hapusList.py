# hapus dengan remove()
# remove hanya menghapus elemen pertama yang dijumpai
my_list = ['p','y','t','h','o','n','p']
my_list.remove('p')
print(my_list)

# dari yg awalnya ['y', 't', 'h', 'o', 'n', 'p']
# dan hapus index ke 2 nya yaitu 'h'
del my_list[2]
print(my_list)

# hapus dengan clear()
my_list.clear()
# hasil output : []
print(my_list)



