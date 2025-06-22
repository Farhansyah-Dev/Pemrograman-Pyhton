buku_telepone = {
    'Andi' : '08123456789',
    'Budi' : '08198765432',
    'Citra' : '08234567890'
}

# Pencarian Nomor Telephone 
namaDicari = 'Farhan'

if namaDicari in buku_telepone:
    print (f'{namaDicari} adalah {buku_telepone [namaDicari]}')
else:
    print (f'{namaDicari} tidak ditemukan di daftar kontak')
    
    
#Contoh Penggunaan Dictionary
hashTable = {}

#Menambahkan Item / Elemen
hashTable['nama'] = 'Farhan'
hashTable['umur'] = 21
hashTable ['city'] = 'Bekasi'

print(f'Hash Table {hashTable}')

#Akses Cepat Dengan Key
print(f'nama: {hashTable ['nama']}')