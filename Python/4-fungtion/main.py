#Definisi Fungsi
# Fungsi adalah blok kode yang digunakan untuk menjalankan tugas tertentu dan dapat dipanggil berulang kali.
# Fungsi membuat kode lebih modular, mudah dikelola, dan digunakan kembali.

#STRUKTUR DASAR FUNGSI
# Deklarasi Fungsi: Mendefinisikan nama, parameter, dan tipe return.
# Pemanggilan Fungsi: Menjalankan fungsi dari dalam program utama atau fungsi lainnya.
# Return Value: Nilai yang dikembalikan oleh fungsi, jika ada.

#Sintaks Dasar Fungsi
def tambah (a, b):
    return a + b
#Pemanggilan Fungsi
hasil = tambah (5, 7) #Mengembalikan nilai 12
print(f'Hasil penjumlahan kedua bilangan {hasil}')

#Sintaks fungsi tanpa parameter
def pesan():
    print("Selamat datang di Python")
    print("Semoga harimu menyenankan")
# Memanggil fungsi
pesan()

#Studi Kasus Fungsi Untuk Penghitung Luas Lingkaran
def hitung_luas (r):
    return 3.14 * r * r

jari_jari = float(input('Masukan jari-jari lingkaran: '))
print(f'Luas Lingkaran' , hitung_luas(jari_jari))

#FUNGSI REKURSIF
#Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri. Digunakan untuk menyelesaikan masalah yang dapat dipecah menjadi sub-masalah yang lebih kecil

def faktorial (n):
    if n <= 1:
        return 1
    else:
        return n * faktorial (n - 1)
print (f'Faktorial dari 5 adalah {faktorial(5)}')

#STUDI KASUS KALKULATOR SEDERHANA
def tambah (a, b):
    return a + b

def kurang (a, b):
    return a - b

def perkalian (a, b):
    return a * b

def pembagian (a, b):
    return a / b

print(f'Hasil Penjumlahan {tambah(10, 2)}')
print(f'Hasil Penjumlahan {kurang(10, 2)}')
print(f'Hasil Penjumlahan {perkalian(10, 2)}')
print(f'Hasil Penjumlahan {pembagian(10, 2)}')

#FUNGSI DENGAN DEFAULT PARAMETER
def salam (nama="Muhammad Farhan Wirdiansyah"):
    print(f"Hay {nama} Selamat pagi")

#Memanngil fungsi
salam()

#Memanggil fungsi dengan argumrn
salam("Andi")

#STUDI KASUS MENENTUKAN BILANGAN PRIMA
def cek_prima (n):
    #bilangan prima adalah bilangan yang lebih dari 1
    if n <= 1:
        return False
    
    #bilangan prima tidak dapat dibagi dengan bilangan lain kecuali 1 dan dirinya sendiri
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

angka = int(input('Masukan sebuah angka: '))

#mengecek apakah angka tersebut adalah bilangan prima
if cek_prima(angka):
    print(f'{angka} adalah bilangan prima')
else:
    print(f'{angka} bukanlah bilangan prima')
    
#STUDI KASUS MENGHITUNG JARAK TEMPUH
def hitung_jarak (kecepatan, waktu):
    return kecepatan * waktu
#input user
kecepatan = int(input('Masukan kecepatan (km/jam): '))
waktu = float(input('Masukan waktu tempuh (jam): '))

#menghitung jarak tempuh
jarak = hitung_jarak(kecepatan, waktu)
print(f'jarak yang ditempuh: {jarak} km')