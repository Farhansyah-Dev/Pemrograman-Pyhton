#Menentukan apakah bilangan tersebut negatif dan positif

angka = int(input("Masukan Angka: ")) #memina input dari user
#inputan dari user disimpan dalam variabel angka

if angka < 0: #jika angka kurang dari 0
    print("Bilangan Negatif") #maka cetak bilangan negatif
    
elif angka > 0: #jika angka lebih dari 0
    print("Bilangan Positif") #maka cetak bilangan positif
else: #else jika tidak memenuhi syarat diatas
    print("Angka Nol") #maka cetak angka nol