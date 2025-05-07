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
    if angka == 5:
        break
print("Selesai")