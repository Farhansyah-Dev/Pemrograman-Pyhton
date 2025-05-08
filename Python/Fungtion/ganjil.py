
# Mengecek bilangan ganjil

def ganjil():
    """Fungsi untuk mengecek bilangan ganjil"""
    num = int(input("Masukan Angka:"))
    if num % 2 != 0:
        print (f"{num} Bilangan ganjil")
    else:
        print (f"{num} Bilangan genap")

ganjil ()