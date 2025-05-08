#Membuat program untuk mengakses data dari list
#Membuat list

#inisialisasi list kosong
list_buah = []

#menambahkan elemen ke dalam list
list_buah.append("Mangga") #menambahkan buah mangga kedalam list_buah
list_buah.append("Jeruk") #menambahkan buah jeruk kedalam list_buah
list_buah.append("Pisang") #menambahkan buah pisang kedalam list_buah

print(list_buah [1]) #menampilkan elemen kedua list_buah
print(list_buah [0]) #menampilkan elemen pertama list_buah

print(f"isi dari kerangjang list_buah adalah {list_buah}") #menampilkan isi dari list_buah

list_buah[1] = "Leci" #mengubah elemen kedua list_buah menjadi leci
print(f"Setelah buah jeruk diganti menjadi leci, isi dari keranjang list_buah adalah {list_buah}") #menampilkan isi dari list_buah setelah mengubah elemen kedua