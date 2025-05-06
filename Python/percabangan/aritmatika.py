# Kalkulator sederhana menggunakan percabangan 
# Menggunakan if, elif, else
# Menggunakan input dari user
# Menggunakan operator aritmatika
# Menggunakan operator logika
# Menggunakan operator perbandingan
# Menggunakan operator penugasan

operasi = input("Pilih operasi yang diinginkan (+, -, *, /): ")
angka1 = int(input("Masukan angka pertama: "))
angka2 = int(input("Masukan angka kedua: "))

operasi = operasi.strip() #menghilangkan spasi di awal dan akhir string

if operasi == "+":
    print(f"Hasil dari penjumlahan {angka1} + {angka2} = {angka1 + angka2}")

elif operasi == "-":
    print(f"Hasil dari pengurangan {angka1} - {angka2} = {angka1 - angka2}")
    
elif operasi == "*":
    print(f"Hasil dari perkalian {angka1} x {angka2} = {angka1 * angka2}")
    
elif operasi == "/":
    print(f"Hasil dari pembagian {angka1} : {angka2} = {angka1 / angka2}")

else:
    print("Operasi yang anda masukan tidak valid")
