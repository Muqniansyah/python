my_list = ["I", "love", "python", "programming", 2017]
# output : I
my_list[0]

# output : python
my_list[2]

# # list dalam list
your_list = ["hello", [1, 2, 3], "python"]

# # output : 1
print(your_list[1][0])

# # output : 3
print(your_list[1][2])

# # output : IndexError
my_list[6]