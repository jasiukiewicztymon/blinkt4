from colorama import init as colorama_init
from colorama import Fore, Back, Style
from os import system as cmd
from getch import getch
from blinkt import set_pixel, set_brightness, show, clear, set_all

import duo

def printmenu(index):
    cmd('clear')

    # Input game mode
    print(f"\n\t{Fore.CYAN}{Style.DIM}{Style.BRIGHT}Welcome to Blinkt4\n{Style.RESET_ALL}")
    
    # {Style.BRIGHT}
    options = [
        f"\t{Fore.MAGENTA}Solo Game Vs AI{Style.RESET_ALL}",
        f"\t{Fore.MAGENTA}Duo Game{Style.RESET_ALL}",
        f"\t{Fore.MAGENTA}Multiplayer Game{Style.RESET_ALL}",
        f"\t{Fore.MAGENTA}About Creators{Style.RESET_ALL}",
        f"\t{Fore.MAGENTA}Quit{Style.RESET_ALL}\n"
    ]
    
    for i in range(len(options)):
        if i == index:
            print(f"{Style.BRIGHT}", end="")
        print(options[i])
    
    valid = False
    
    choice = getch()
    if choice == '\n':
        valid = True
    elif choice == '\x1b':
        pass
    elif choice == '\t':
        index = index + 1
        if index == len(options):
            index = 0
        
    cmd('clear')
    return index, valid

# Game Loop
while True:
    # blinkt
    set_brightness(0.1)
    set_all(0, 255, 255)
    show()
    
    index = 0
    valid = False
    while not valid:
        index, valid = printmenu(index)    
    
    if index == 4:
        break
    elif index == 3:
        print(f"\n\t{Fore.CYAN}{Style.DIM}{Style.BRIGHT}Blinkt4 creators\n{Style.RESET_ALL}")
        
        print(f"\t{Fore.MAGENTA}{Style.DIM}{Style.BRIGHT}Jasiukiewicz Tymon{Style.RESET_ALL} - {Fore.MAGENTA}Multiplayer mode & Game & Interface{Style.RESET_ALL}")
        print(f"\t{Fore.MAGENTA}{Style.DIM}{Style.BRIGHT}Perrinjaquet Timéo{Style.RESET_ALL} - {Fore.MAGENTA}Game & Interface{Style.RESET_ALL}\n")
        
        getch()
    elif index == 2:
        print(f"\n\t{Fore.CYAN}{Style.DIM}{Style.BRIGHT}Welcome to multiBlinkt4\n{Style.RESET_ALL}")
        print(f"\t{Fore.RED}{Style.BRIGHT}STILL IN DEVELOPEMENT\n{Style.RESET_ALL}")
        
        getch()
    elif index == 1:
        duo.play()
    else:
        print(f"\n\t{Fore.CYAN}{Style.DIM}{Style.BRIGHT}Welcome to soloBlinkt4\n{Style.RESET_ALL}")
        print(f"\t{Fore.RED}{Style.BRIGHT}STILL IN DEVELOPEMENT\n{Style.RESET_ALL}")
        
        getch()
        
