#percabangan switch case pada python menggunakan function
def switch_case(hari):
    match hari:
        case 1:
            print("Senin")
        case 2:
            print("Selasa")
        case 3:
            print("Rabu")
        case 4:
            print("Kamis")
        case 5:
            print("Jumat")
        case 6:
            print("Sabtu")
        case 7:
            print("Mnggu")
        case _:
            print("Hari tidak valid") #jika tidak ada case yang cocok maka akan menampilkan ini
            return hari
hari = int(input("Masukan hari (1-7): "))
switch_case(hari) #memanggil function switch_case dengan parameter hari