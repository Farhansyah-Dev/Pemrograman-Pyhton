#Membuat program Menggunakan For Loop
#  For Loop
#  for loop adalah perulangan yang terhitung (counted loop) yang digunakan untuk melakukan perulangan sebanyak n kali.
# for loop terdiri dari 3 bagian yaitu inisialisasi, kondisi, dan increment/decrement.
# berikut adalah rumus dari for loop:
# for(inisialisasi; kondisi; increment/decrement){
#statement;
# }
# inisialisasi adalah bagian yang digunakan untuk menginisialisasi variabel yang digunakan dalam for loop.
#  kondisi adalah bagian yang digunakan untuk menentukan kapan for loop akan berhenti.
# increment/decrement adalah bagian yang digunakan untuk menambah atau mengurangi nilai variabel yang digunakan dalam for loop.
# berikut contoh penggunaan for loop:
#Menggunakan For Loop untuk mencetak angka dari 1 hingga 10

for i in range (1, 11): #inisialisasi
    print(f"Angka ke-{i}") #kondisi
print("Selesai") #increment/decrement
# #=========================================================================

# STUDI KASUS MENGHITUNG JUMLAH RATA RATA

# INISIALISASI 
angka_list = []

# INPUT DATA
while True: #perulangan tak terhingga
    angka = float(input("Masukan angka (masukan angka negatif untuk berhenti): ")) #input dari user
    if angka < 0: #jika angka kurang dari 0
        break #keluar dari perulangan
    angka_list.append(angka) #menambahkan angka ke dalam list

# MENGHITUNG JUMLAH DAN RATA RATA
jumlah = 0 #inisialisasi jumlah
for angka in angka_list: #perulangan untuk menghitung jumlah
    jumlah += angka #menambahkan angka ke dalam jumlah

# MENGHITUNG RATA RATA
if len(angka_list) > 0: #jika panjang list lebih dari 0
    rata_rata = jumlah / len(angka_list)
else: #jika panjang list sama dengan 0
    rata_rata = 0
    
# MENAMPILKAN HASIL
print(f"Jumlah: {jumlah}") #menampilkan jumlah  
print(f"Rata-rata: {rata_rata}") #menampilkan rata-rata
    