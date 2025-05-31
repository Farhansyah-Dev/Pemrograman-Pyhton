import socket
from time import sleep

pc_user = socket.gethostname()

def welcome_message():
    style = "*" * (len(pc_user)+8)
    print(style)
    print(f"*** {pc_user} ***")
    print(style)
    
def exit_game():
    print("Game segera berakhir.")
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    print('Game berakhir')
    
if __name__ == "__main__":
    welcome_message()
    exit_game()