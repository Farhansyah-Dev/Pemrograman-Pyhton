#if else
#if else adalah percabangan yang paling sederhana
# #Syntax:
# if kondisi:
#     #kode yang akan dieksekusi jika kondisi benar
# else:
#     #kode yang akan dieksekusi jika kondisi salah
#
# #Contoh:

a = 100
b = 50 

if a > b:
    print("a lebih besar dari b")
else:
    print("a lebih kecil dari b")
    
# KALKULAATOR SEDERHANA IF ELSE
# #Menggunakan input dari user
# #Menggunakan operator aritmatika
# #Menggunakan operator logika
# #Menggunakan operator perbandingan
# #Menggunakan operator penugasan
# operasi = input("Pilih operasi yang diinginkan (+, -, *, /): ")

operasi = input("Pilih operasi yang diinginkan (+, -, *, /): ") #input dari user
# #Menggunakan operator aritmatika
angka1 = int(input("Masukan angka pertama: ")) #input dari user
angka2 = int(input("Masukan angka kedua: ")) #input dari user

operasi = operasi.strip() #menghilangkan spasi di awal dan akhir string

if operasi == "+": #if digunakan untuk mengeksekusi kode jika kondisi benar
    print(f"Hasil dari penjumlahan {angka1} + {angka2} = {angka1 + angka2}") #menggunakan f-string untuk menampilkan hasil

elif operasi == "-": #elif digunakan untuk mengeksekusi kode jika kondisi sebelumnya salah
    print(f"Hasil dari pengurangan {angka1} - {angka2} = {angka1 - angka2}") 
    
elif operasi == "*": 
    print(f"Hasil dari perkalian {angka1} x {angka2} = {angka1 * angka2}")
    
elif operasi == "/":
    print(f"Hasil dari pembagian {angka1} : {angka2} = {angka1 / angka2}")

else: #else digunakan untuk mengeksekusi kode jika semua kondisi sebelumnya salah
    print("Operasi yang anda masukan tidak valid")
    
#=========================================================================
# IF ELSE BERSARANG
lama_menginap = int(input("Berapa lama menginap?: ")) #input dari user
harga_permalam = 300000 #harga per malam
total_harga = lama_menginap * harga_permalam #total harga
diskon = 0 #diskon awal

if total_harga >= 1000000: #jika total harga lebih dari sama dengan 1 juta
    keterangan = "Diskon 30%" #keterangan diskon
    diskon = 0.2 * total_harga #diskon 20%
    if lama_menginap >= 5: #jika lama menginap lebih dari sama dengan 5 malam
        bonus = print("Bonus 1 malam gratis") #bonus 1 malam gratis
    else: #jika lama menginap kurang dari 5 malam
        bonus = print("Tidak ada bonus") #tidak ada bonus
else: #jika total harga kurang dari 1 juta
    keterangan = "Tidak ada diskon" #keterangan tidak ada diskon
    diskon = 0 #diskon 0
if lama_menginap < 5: #jika lama menginap kurang dari 5 malam
    keterangan = "Diskon 10%" #keterangan diskon
    diskon = 0.1 * total_harga #diskon 10%
    bayar = total_harga - (total_harga * 0.1) #bayar akhir
else: #jika lama menginap lebih dari sama dengan 5 malam
    bayar = total_harga  #bayar akhir
print(f"Total Harga: Rp. {total_harga}") #menampilkan total harga
print(f"Keterangan : {keterangan}") #menampilkan keterangan
print(f"Diskon     : {diskon}") #menampilkan diskon
print(f"Bayar akhir: {bayar}")  #menampilkan bayar akhir
# #=========================================================================

# MENETUKAN BILANGAN POSITIF DAN NEGATIF
# #Menggunakan input dari user

#Menentukan apakah bilangan tersebut negatif dan positif

angka = int(input("Masukan Angka: ")) #memina input dari user
#inputan dari user disimpan dalam variabel angka

if angka < 0: #jika angka kurang dari 0
    print("Bilangan Negatif") #maka cetak bilangan negatif
    
elif angka > 0: #jika angka lebih dari 0
    print("Bilangan Positif") #maka cetak bilangan positif
else: #else jika tidak memenuhi syarat diatas
    print("Angka Nol") #maka cetak angka nol
    
    
# #=========================================================================
# MENENTUKAN NILAI KELULUSAN BERDASARKAN NILAI
# #Menggunakan input dari user
#menentukan kelulusan siswa berdasarkan nilai
nilai = int(input("Masukan Nilai: ")) #memina input dari user


if nilai >= 70: #jika nilai lebih dari sama dengan 70
    print("Lulus") #maka cetak lulus
    
else: #jika nilai kurang dari 70
    print("Tidak Lulus")
# #=========================================================================
# CONTOH IF ELSE PEMESANAN 
# Program pemesanan if else
# Input
# Nama pemesan

banyak_barang = int(input("Mau pesan berapa banyak? "))
harga = int(input("Harga per barang Rp: "))

jumlah = banyak_barang * harga
diskon = 0

if jumlah >= 100000:
    diskon = 0.1 * jumlah
    print(f"Diskon 10%: Rp {diskon}")
    
bayar = jumlah - diskon
print(f"Total yang harus dibayar: Rp {bayar}")
# #=========================================================================
# PROGRAM SUATU KONDISI MENGGUNAKAN SWITCH CASE

#percabangan switch case pada python menggunakan function
def switch_case(hari):
    match hari:
        case 1:
            print("Senin")
        case 2:
            print("Selasa")
        case 3:
            print("Rabu")
        case 4:
            print("Kamis")
        case 5:
            print("Jumat")
        case 6:
            print("Sabtu")
        case 7:
            print("Mnggu")
        case _: 
            print("Hari tidak valid") #jika tidak ada case yang cocok maka akan menampilkan ini
            return hari 
hari = int(input("Masukan hari (1-7): ")) #input dari user
switch_case(hari) #memanggil function switch_case dengan parameter hari