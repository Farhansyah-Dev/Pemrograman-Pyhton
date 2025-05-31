import datetime
import os

class mahasiswa:
    def __init__(self,nama,NIM,kelas,studi,semester,status):
        self.nama = nama
        self.NIM = NIM
        self.kelas = kelas
        self.studi = studi
        self.semester = semester
        self.status = status

    def tampilkan_data (self):
        print (f'Nama Mahasiswa\t: {self.nama}')
        print (f'NIM\t: {self.NIM}')
        print (f'Kelas\t: {self.kelas}')
        print (f'Studi\t: {self.studi}')
        print (f'Semester\t: {self.semester}')
        print (f'Ststus\t: {self.status}')
        
    def input_data(self):
        nama = input('Nama Mahasiswa: ')
        nim = int(input('NIM: '))
        kelas = input('Kelas: ')
        studi = input('Studi: ')
        semester = int(input('Semester: '))
        status = input('Status: ')
        return mahasiswa (nama, nim, kelas, studi, semester, status)

os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    print(f'Selamat Datang')
    print(f'Data Mahasiswa')
    
    mahasiswa.input_data()
    mahasiswa.tampilkan_data()


    