a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

if a > b and a > c:
    terbesar = a
    print("Angka terbesar adalah:", terbesar)
elif b > a and b > c:
    terbesar = b
    print("Angka terbesar adalah:", terbesar)
elif c > a and c > c:
    terbesar = c
    print("Angka terbesar adalah:", terbesar)
else :
    print("tidak ada nilai terbesar")

