#JENIS JENIS STRUKTUR DATA
# - ARRAY : Struktur data linear yang menyimpan elemen dengan ukuran tetap
# - list : struktur data dinamis yang dapat menyimpan elemen dengan ukuran yang bervariasi
# - Stack : Struktur data berbasis LIFO (Last in, First Out)
# - Queue : Struktur data berbasis FIFO (First In, First Out)
# - Dictionary : Struktur data yang menyimpan pasangan key-value

#CONTOH LIST DI PYTHON
arr = [10, 20, 30, 40, 50] #inisialisasi list dengan nilai awal
#menampilkan elemesn list dengan for
for i in range(len(arr)):
    print(f'uruta ke-{i}: {arr[i]}')
    
#OPERASI DASAR PADA LIST 
# menambah elemen : menambahkan elemen baru kedalam list
# menghapus elemen : menghapus elemen tertentu dari list
# mengakses elemen : mengakses elemen tertentu dari list

angka = [] #deklarasi list kosong

#menambahkan elemen kedalam list kosong
angka.append(1) #menambahkan elemen 1
angka.append(2) #menambahkan elemen 2
angka.append(3) #menambahkan elemen 3

#menampilkan elemen list
print (f'Elemen dalam list: {angka}')

#menambah elemen list lagi
angka.append(5) #menambahkan elemen 4
print(f'Setelah menambah elemen 4: {angka}')

#MENGAKSES ELEMEN LIST
angka_pertama = angka[0]
angka_kedua = angka[1]
angka_ketiga = angka [2]
angka_terakhir = angka[-1]
#menampilkan elemen yang diakses
print(f'Angka Pertama: {angka_pertama}')
print(f'Angka Kedua: {angka_kedua}')
print(f'Angka Ketiga: {angka_ketiga}')
print(f'Angka Terakhir: {angka_terakhir}')

angka[-1] = 4 #mengubah nilai elemen terakhir
print(f'Elemen list setelah diubah: {angka}')