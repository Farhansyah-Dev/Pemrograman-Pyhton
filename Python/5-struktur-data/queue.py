#Queue adalah struktur data FIFO (Firts in, First Out).

from collections import deque

queue = deque([10, 20, 30])
print(f'Elemen depan {queue[0]}') #Menampilkan elemen terdepan

queue.popleft() #menghapus elemen depan
print(f'{queue[0]}')