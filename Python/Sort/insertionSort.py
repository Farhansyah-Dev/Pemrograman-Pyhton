def InsertionSort (arr):
    n = len (arr) # Dapatkan Panjang Array
    
    if n <= 1:
        return arr# Jika Array memiliki 1 atau kurang elemen, maka Array sudah terurut
    
    for i in range (1, n): # Ulangi array mulai dari elemen kedua
        key = arr [i] # Simpan elemen saat ini ke dalam variabel key
        j = i - 1 # Simpan index elemen sebelumnya ke dalam variabel j
        while j >= 0 and key < arr [j]:
            #pindahkan elemen yang lebih besar
            arr [j + 1] = arr [j] # Pindahkan elemen kekanan
            j -= 1 # Kurangi index j
            arr[j + 1] = key #Masukan kunci pada posisi yang tepat
# Mengurutkan array [40, 30, 22, 8, 18, 10, 71]
arr = [40, 30, 22, 8, 18, 10, 71]
print (f'Elemen sebelum di urutkan: \n {arr}')
print (f'Elemen setelah di urutkan')
InsertionSort(arr)
print(arr)
    