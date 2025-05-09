# OOP adalah paradigma pemrograman yang berorientasi pada objek. bukan hanya sekedar fungsi dan prosedur..
# OOP adalah cara untuk mengorganisir kode agar lebih terstruktur dan mudah dipahami.
# OOP memungkinkan pemodelan program dengan lebih mendekati kehidupan nyata, melalui konsep seperti objek, kelas, pewarisan, dan polimorfisme. 

# Kelas: Template atau blueprint untuk membuat objek.
# Objek: Instansiasi dari kelas yang memiliki data dan fungsi.
# Enkapsulasi: Menyembunyikan data dan hanya memperlihatkan fungsi yang dibutuhkan.
# Pewarisan: Memungkinkan kelas baru untuk mewarisi sifat dari kelas yang ada.
# Polimorfisme: Kemampuan satu fungsi untuk bekerja dalam cara yang berbeda.


#__init__ adalah konstruktor yang digunakan untuk menginisialisasi atribut nama dan umur.

#self adalah referensi ke objek saat ini. Ini digunakan untuk mengakses atribut dan metode dalam kelas.


# Contoh sederhana OOP
class Mahasiswa:
    def __init__ (self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")

# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("budi", "312410067", "Teknik Informatika")
mahasiswa2 = Mahasiswa("siti", "312410068", "Teknik Informatika")
mahasiswa3 = Mahasiswa("andi", "312410069", "Teknik Informatika")

# Menampilkan informasi mahasiswa
mahasiswa1.info()


#=======================================================================
#Enkapsulasi adalah cara untuk menyembunyikan data dalam kelas dan hanya memperlihatkan metode tertentu.
# Atribut yang dienkapsulasi biasanya ditandai dengan garis bawah di Python (_nama) atau akses privat di C++ (private).

#ENKAPSULASI
class Mahasiswa:
    def __init__ (self, nama, nim, prodi):
        self.__nama = nama
        self.__nim = nim
        self.__prodi = prodi
        
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_nim(self):
        return self.__nim
    
    def set_nim(self, nim):
        self.__nim = nim
        
    def get_prodi(self):
        return self.__prodi
    
    def set_prodi(self, prodi):
        self.__prodi = prodi
    
mhs = Mahasiswa("budi", "312410067", "Teknik Informatika")
print("Nama: ", mhs.get_nama())
print("NIM: ", mhs.get_nim())
print("Prodi: ", mhs.get_prodi())


#=======================================================================
#PEWARISAN
# Pewarisan adalah cara untuk membuat kelas baru yang mewarisi atribut dan metode dari kelas yang sudah ada.
# Kelas yang mewarisi disebut subclass, sedangkan kelas yang diwarisi disebut superclass
# Dalam pewarisan, kita dapat menambahkan atribut dan metode baru pada subclass tanpa mengubah superclass.

# Contoh pewarisan
class Orang:
    def menyapa (self):
        print("Halo, saya adalah orang.")

class Mahasiswa(Orang):
    def belajar (self):
        print("Saya sedang belajar.")
        
# Membuat objek dari kelas Mahasiswa
mahasiswa = Mahasiswa()
mahasiswa.menyapa()
mahasiswa.belajar()