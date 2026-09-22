n = int(input("Masukkan batas nilai n: "))

a, b = 0, 1
print("Deret Fibonacci:")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b