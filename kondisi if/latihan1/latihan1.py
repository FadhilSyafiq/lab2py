a = int(input("masukkan bilangan pertama:"))
b = int(input("masukkan bilangan kedua:"))
c = int(input("masukkan bilangan ketiga:"))
d = int(input("masukkan bilangan keempat:"))

angkaTerbesar = a
if b > angkaTerbesar:
    angkaTerbesar = b
    if c > angkaTerbesar:
        angkaTerbesar = c
        if d > angkaTerbesar:
            angkaTerbesar = d

            print("Angka", angkaTerbesar, "adalah yang terbesar dari keempat angka tersebut.")
