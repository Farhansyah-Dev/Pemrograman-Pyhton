#Di Python, Dictionary adalah struktur data yang menyimpan data dalam bentuk pasangan (key:value).

#deklarasi Dictionary
#Dictionnary mahasiswa menyimpan data dalam bentuk pasangan key-value
#contoh pasangan key-value: "nama" : "farhan"

#Operasi pada Dictionary
# 1. Mengakses elemen dengan menggunakan key, misalnya mahasiswa["nama"].
# 2. Menambah elemen baru dengan menambahkan key-value baru: mahasiswa["universitas"] = "Universitas Pelita Bangsa"
# 3. Mengubah nilai elemen dengan key yang sudah ada, misalnya: mahasiswa["umur"] = 21
# 4. Menghapus elemen dengan menggunakan del, misalnya: mahasiswa ["jurusan"].

#Deklarasi Dictionary
mahasiswa = {
    "nama" : "Muhammad Farhan Wirdiansyah",
    "NIM"  : 312410067,
    "kelas": "TI.24.C2",
    "prodi": "Teknik Informatika",
    "umur" : 22
}
#Mengakses Elemen Dictionary
print("nama: ", mahasiswa["nama"])
print("NIM: ", mahasiswa["NIM"])
print("kelas: ", mahasiswa["kelas"])
print("prodi: ",mahasiswa["prodi"])

#menambah elemen Dictionnary
mahasiswa["universitas"] = "Universitas Pelita Bangsa"
mahasiswa["tahun masuk"] = 2024

#mengubah nilai (value) Dictionary
mahasiswa["kelas"] = "TI.24.C3"

#menghapus elemen Dictionary
del mahasiswa ["umur"]

print(f"{mahasiswa}")