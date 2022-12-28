#Fibonacci Secara Rekursif
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-1) +
fibonacci(n-2))
x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))
print("Deret Fibonacci")
for i in range(x):
    print(fibonacci(i),end=' ')

# hitung fibonanci
# 0,1,1,2,3
# 0+1=1,1+1=2,2+1=3