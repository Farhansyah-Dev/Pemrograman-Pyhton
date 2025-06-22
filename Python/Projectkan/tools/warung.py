import main

def start():
    print('Warung Mini APPS.')
    nama = input('Masukan nama kamu ya: ')
    
    harga = int(input('Total Belanja Rp:'))
    
    uang_user = int(input(f'Uang yang {nama} gunakan Rp:'))
    
    if uang_user < harga:
        print(f'Maaf {nama} uang kamu belum cukup nih...')
        main.exit_game()
        main.menu()
        
    elif uang_user > harga:
        print(f'Kembalian {nama} Rp: {uang_user - harga}')
        main.menu()
        
    else:
        if harga == 0 :
            print(f'{nama} belum melakukan transaksi...')
            kembali_menu = input('kembali ke menu? [yes/no] ')
            if kembali_menu.lower() == 'yes':
                main.menu()
            else:
                print('Terima kasih telah menggunakan aplikasi kami!')
                main.exit_game()

if __name__ == '__main__':
    start()