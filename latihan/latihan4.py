#string
var1 = 'hello python'
var2 = "programming with python"
print (var1)
print (var2)

print("====================")

#mengakses nilai string
var3 = 'Hello python'
var4 = "I love python"
print("var3[0]", var3[0])
print("var4[2:13] :", var4[2:13])

print("====================")

#mengupdate string
var5 = 'Hello python!'
var6 = var5[:6]
print(var5)
print("String update: -", var5[:6] + 'world')


print("====================")

#menggabung string
str1 = 'Hello'
str2 = 'python'
    #menggunakan +
print('str1 + str2 =', str1 + str2)
    #menggunakan *
print('str1 * 3 =', str1 * 3)

print("====================")

#mengetahui panjang string
string = 'i love python'
print(len(string))