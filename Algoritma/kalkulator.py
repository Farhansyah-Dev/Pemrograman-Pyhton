def tambah (angka1, angka2):
    return angka1 + angka2
def kurang (angka1, angka2):
    return angka1 - angka2
def kali (angka1, angka2):
    return angka1 * angka2
def bagi (angka1, angka2):
    return angka1 / angka2
def pangkat (angka1, angka2):
    return angka1 ** angka2
def modulus (angka1, angka2):
    return angka1 % angka2

def main ():
    while True:
        print ('\n---Aplikasi Kalkulator---')
        print ('1. Penjumlahan')
        print ('2. Pengurangan')
        print ('3. Perkalian')
        print ('4. Pembagian')
        print ('5. Perpangkatan')
        print ('6. Modulus')
        print ('7. Keluar')
        
        userInput = input ("Pilih Operasi (1 - 6): ")
        if userInput in ('1', '2', '3', '4', '5', '6'):
            angka1 = int(input('Masukan angka: '))
            angka2 = int(input('Masukan angka: '))
            
            if userInput == '1':
                print ('Hasil Penjumlahan = ', tambah(angka1, angka2))
            elif userInput == '2':
                print ('Hasil Pengurangan = ', kurang(angka1, angka2))
            elif userInput == '3':
                print ('Hasil Perkalian = ', kali(angka1, angka2))
            elif userInput == '4':
                print ('Hasil Pembagian = ', bagi(angka1, angka2))
            elif userInput == '5':
                print ('Hasil Perpangkatan = ', pangkat(angka1, angka2))
            elif userInput == '6':
                print ('Hasil Modulus = ', modulus(angka1, angka2))
            else: 
                print ('Pilihan Tidak Valid')
                break
            
            print('Program Berakhir')
        
main()