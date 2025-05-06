# Program Percabangan if else bersarang

lama_menginap = int(input("Berapa lama menginap?: "))
harga_permalam = 300000
total_harga = lama_menginap * harga_permalam
diskon = 0

if total_harga >= 1000000:
    keterangan = "Diskon 30%"
    diskon = 0.2 * total_harga
    if lama_menginap >= 5:
        bonus = print("Bonus 1 malam gratis")
    else:
        bonus = print("Tidak ada bonus")
else:
    keterangan = "Tidak ada diskon"
    diskon = 0
if lama_menginap < 5:
    keterangan = "Diskon 10%"
    diskon = 0.1 * total_harga
    bayar = total_harga - (total_harga * 0.1)
else:
    bayar = total_harga 
print(f"Total Harga: Rp. {total_harga}")
print(f"Keterangan : {keterangan}")
print(f"Diskon     : {diskon}")
print(f"Bayar akhir: {bayar}")