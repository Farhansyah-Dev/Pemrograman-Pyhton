#Membuat program Menggunakan While Loop
# // While Loop
#     // while loop adalah salah satu jenis perulangan yang ada di C++ yang digunakan untuk mengulang blok kode selama kondisi yang diberikan bernilai benar (true)
#     // while loop memiliki 2 jenis yaitu: while loop dan do while loop
#     // 1. while loop: perulangan akan dilakukan jika kondisi bernilai benar (true)
#     // berikut adalah rumus penggunaan while loop di C++:
#     // while (kondisi) {
#     //     // blok kode yang akan diulang
#     // }
#     // perulangan while akan terus berjalan selama kondisi yang diberikan bernilai benar (true) dan jika kondisi bernilai salah (false), maka perulangan akan berhenti
#     // berikut contoh penggunaan while loop di C++:

#Menggunakan While Loop untuk mencetak angka dari 1 hingga 10
angka = 1
while angka <= 10:
    print(f"Angka ke-{angka}")
    angka += 1

print("Selesai")

#program Menggunakan While Loop break
# // Break
#     // break adalah pernyataan yang digunakan untuk menghentikan perulangan pada saat kondisi tertentu terpenuhi
#     // break dapat digunakan pada semua jenis perulangan seperti for loop, while loop, dan do while loop
#     // berikut adalah contoh penggunaan break pada while loop:
#Menggunakan While Loop untuk mencetak angka dari 1 hingga 10
angka = 1
while angka <= 10:
    print(f"Angka ke-{angka}")
    if angka == 6: #jika angka sama dengan 6
        break #keluar dari perulangan
    angka += 1
print("Selesai")

#program Menggunakan While Loop continue
# // Continue
#     // continue adalah pernyataan yang digunakan untuk melanjutkan perulangan pada saat kondisi tertentu terpenuhi
#Example
angka = 0
while angka < 10:
    angka += 1
    if angka == 5: #jika angka sama dengan 5
        continue #lanjutkan ke perulangan berikutnya
    print (f"angka ke-{angka}")
print("Selesai") 

#program Menggunakan While Loop else
# // Else
#     // else adalah pernyataan yang digunakan untuk mengeksekusi blok kode setelah perulangan selesai
#     // else dapat digunakan pada semua jenis perulangan seperti for loop, while loop, dan do while loop
#Example

angka = 0
while angka < 10: #jika angka kurang dari 10
    angka += 1 #tambahkan angka 1
    print (f"angka ke-{angka}")
else: #jika angka lebih dari 10
    print("Perulangan selesai")
    
