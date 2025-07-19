# program implementasi BubbleSort

def bubbleSort (arr): # membuat fungsi Bubblesort
    panjangArray = len(arr) #Variable panjang data array
    
    #Algoritma BubbleSort
    for putaran in range (panjangArray): # perulangan luar
        tukarPosisi = False
        for index in range (0, panjangArray - putaran-1): #Perulangan dalam
            if (arr[index] > arr[index+1]): #Jika elemen lebih besar dari elemen setelahnya maka tukar posisi
                arr[index], arr[index+1] = arr[index+1], arr[index]
                
        if (tukarPosisi == True): #Jika tukar posisi dilakukan maka menghentikan bubblesort
            break
if __name__ == "__main__": #sintaks python dalam menjalankan code program
    arr = [78, 14, 81, 9, 10, 1] #Deklarasikan data Array
    print(f'Data array sebelum di bubble sort: {arr}') #Hasil sebelum di BubbleSort
    
    
    bubbleSort(arr) #Memanggil fungtion BubbleSort
    print(f'Data array sebelum di bubble sort: {arr}') #Hasil setelah di BubbleSort
                