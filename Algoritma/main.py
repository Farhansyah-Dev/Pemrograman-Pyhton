
penjualan = [
    [12, 7, 10], #hari 1
    [14, 8, 9], #hari 2
    [13, 6, 11], #hari 3
    [11, 10, 8], #hari 4
    [16, 8, 12], #hari 5
    [14, 6, 9], #hari 6
    [11, 6, 9] #hari 7
]

#hitung Total Penjualan setiap barang selama 7 hari
total_tepung = sum(hari[0] for hari in penjualan)
total_telur = sum(hari[1] for hari in penjualan)
total_gula = sum(hari[2] for hari in penjualan)

#Menampilkan Total dari keseluruhan barang
print (f'Total penjualan Tepung selama 7 hari: {total_tepung}')
print (f'Total penjualan Telur selama 7 hari: {total_telur}')
print (f'Total penjualan Gula selama 7 hari: {total_gula}')

#Cari hari dengan penjualan tertinggi untuk setiap barang
hariTepungMax = max (enumerate(penjualan), key=lambda x: x [1][0])[0] + 1
hariTelurMax = max (enumerate(penjualan), key=lambda x: x [1][1])[0] + 1
hariGulaMax = max (enumerate(penjualan), key=lambda x: x [1][1])[0] + 1

#Menampilkan hari dengan penjualan tertinggi
print (f'Hari dengan Penjualan Tertinggi Tepung: {hariTepungMax}')
print (f'Hari dengan Penjualan Tertinggi Tepung: {hariTelurMax}')
print (f'Hari dengan Penjualan Tertinggi Tepung: {hariGulaMax}')

#Cari Total penjualan semua barang selama 1 minggu
TotalPenjualanSemua = sum (sum (hari) for hari in penjualan )
print (f'Total Penjualan Selama 1 minggu: {TotalPenjualanSemua}' )
