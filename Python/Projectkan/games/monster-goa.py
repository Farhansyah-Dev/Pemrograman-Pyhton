import random
import main

def start():
    nama_user = input('Sebelum main!\nMasukan nama kamu dahulu ya...:')
    while True:
        monster_posisi = random.randint(1, 4)
        goa_visual = "|_|"
        goa = [goa_visual] * 4
        goa_monster = goa.copy()
        goa_monster[monster_posisi - 1] = "|0_0|"
        goa = " ".join(goa)
        goa_monster = " ".join(goa_monster)

        print(f"\nHallo {nama_user}, coba perhatikan Goa dibawah ini:\n\n{goa}\n")
        pilihan_user = int(input(f"Menurut {nama_user}di goa nomor berapa MONSTER berada? [1 / 2 / 3 / 4]: "))
        
        if pilihan_user == monster_posisi:
            print(f'\n {goa_monster}\n\nSelamat {nama_user} kamu berhasil menang! posisi Monster berada di posisi {monster_posisi}') 
        else:
            print(f'\n{goa_monstter}\n\nMaaf!{nama_user} kamu belum berhasil menang! posisi Monster berada di posisi {monster_posisi}')
        
        play_again = input(f'\nApakah {nama_user}ingit melanjutkan gamenya lagi? [Yes / NO]:')       
        if play_again == "No":
            main.menu()

if __name__ == '__main__':
    start()