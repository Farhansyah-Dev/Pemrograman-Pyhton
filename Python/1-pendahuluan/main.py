#Welcome To Python
#This is a simple program to introduce Python
#It will print a welcome message and some basic information about Python

#sintaks
#sintaks adalah aturan atau tata bahasa yang digunakan untuk menulis program dalam bahasa pemrograman
#jika sintaks tidak sesuai maka program tidak akan berjalan

#variabel: ialah tempat menyimpan data 
# (contoh)
x = 5 #ini adalah variabel x yang menyimpan nilai 5
y = "hello" #ini adalah variabel y yang menyimpan nilai string "hello"

#Operator: digunakan untuk melakukan operasi matematika dan logika
#(contoh)
tambah = 5 + 3 #ini adalah operasi penunbuh 5 dan
kurang = 4 - 2 #ini adalah operasi pengurang 4 dan 2
kali = 5 * 4   #ini dalah operasi perkalian
bagi = 10 / 2 #ini adalah operasi pembagian

#Fungsi: ialah blok kode yang menjalankan tugas tertentu (contoh)
def tambah (a,b):
    return a + b
#ini adalah fungsi tambah yang mengembalikan nilai a + b
tambah (6,9)

#Komentar: teks yang tidak dieksekusi, digunakan untuk memberikan catatan pada program 

#Struktur dasar program
#1.fungsi utama : tempat eksekusi program dimulai
#2.Input/Output : tempat program menerima input dan mengeluarkan output
#3.Blok kode : tempat program melakukan tugas tertentu

#Studi kasus program penjumlahan sederhana
angka1 = int(input("Masukan angka pertama :"))
angka2 = int(input("Masukan angka kedua"))
hasil = angka1 + angka2

print(f'Hasil penjumlahan {angka1} + {angka2} = {hasil}')

#Studi kasus input/output sederhana
nama = input("Masukan nama anda:")
umur = int(input('Masukan Umur anda:'))
print(f'Nama anda: {nama}\nUmur anda: {umur}')

#Studi Kasus Program Konversi suhu
suhu_c = int(input('Masukan suhu dalam celcius:'))
farenheit = (9.0/5.0) * suhu_c + 32
print(f'Suhu dalam farenheit {farenheit}')



print ("Hey There!, Hello World!") #ini adalah sintaks untuk mencetak pesan ke layar

#Varible pada python
#Variable
#variable adalah tempat untuk menyimpan data    

#Text Type
nama = "Python" #ini adalah sintaks untuk mendeklarasikan variable nama dengan tipe data string

#Numeric Types
angka = 10 #ini adalah sintaks untuk mendeklarasikan variable angka dengan tipe data integer

koma = 3.14 #ini adalah sintaks untuk mendeklarasikan variable koma dengan tipe data float

#bollean type
#boolean = True #ini adalah sintaks untuk mendeklarasikan variable boolean dengan tipe data boolean
# // Boolean
#     // boolean adalah tipe data yang hanya memiliki dua nilai yaitu True dan False

benar = True #ini adalah sintaks untuk mendeklarasikan variable benar dengan tipe data boolean

salah = False #ini adalah sintaks untuk mendeklarasikan variable salah dengan tipe data boolean

#Urutan atau list type
#list
buah = ['anggur','semangka','mangga']

#tuple
buah = ('anggur','semangka','mangga')

#range
urutan = range(1,10)

#tipe data dictionary
#dictionary
usernamme = {
    "nama" : "Muhammad Farhan Wirdiansyah",
    "umur" : 20,
    "alamat" : "Kp Cisalak 003/004 Kel Sumur Batu, Bantargebang Kota bekasi",
}
