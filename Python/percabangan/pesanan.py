# Program pemesanan if else
# Input
# Nama pemesan

banyak_barang = int(input("Mau pesan berapa banyak? "))
harga = int(input("Harga per barang Rp: "))

jumlah = banyak_barang * harga
diskon = 0

if jumlah >= 100000:
    diskon = 0.1 * jumlah
    print(f"Diskon 10%: Rp {diskon}")
    
bayar = jumlah - diskon
print(f"Total yang harus dibayar: Rp {bayar}")
