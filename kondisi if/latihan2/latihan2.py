# Program Mengurutkan Data

# Input minimal 3 bilangan dari pengguna
bil1 = int(input("bilangan ke-1:"))
bil2 = int(input("bilangan ke-2:"))
bil3 = int(input("bilangan ke-3:"))

# Simpan semua bilangan dalam list
data = [bil1, bil2, bil3]

# Urutkan data dari yang terkecil ke terbesar
data.sort()

# Tampilkan hasil
print("Urutan bilangan", *data)
