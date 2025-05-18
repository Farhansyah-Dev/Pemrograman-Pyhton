#Stack adalah struktur data LIFO (Last in, First Out).
#Fungsi append() menambah elemen ke stack dan pop() menghapus elemen teratas.

stack = [] #inisialisasi stack kosong

stack.append(1) #menambahkan elemen 1
stack.append(2) #menambahkan elemen 2
stack.append(3) #menambahkan elemen 3

print(f'Elemen teratas {stack[-1]}') #menampilkan elemen teratas.

stack.pop() #menghapus elemen teratas.
print(f'Setelah di pop, elemen teratas :{stack[-1]}')

