from libs import welcome_message, exit_game
from games import monster
from tools import warung

def menu():
    user_option = int(input(f'\nmenu program:\n1. Games Monster Goa\n2. Warung Mini\n3. Keluar\n\nsilahkan pilih: '))
    
    if user_option == 1:
        monster.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        main.exit_game()
        
    else:
        print('pilih menu yang tersedia. ')
        
def main():
    welcome_message()
    menu()
    
if __name__=='__main__':
    main()