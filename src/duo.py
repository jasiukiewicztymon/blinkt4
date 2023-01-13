from colorama import init as colorama_init
from colorama import Fore, Back, Style
from os import system as cmd
from getch import getch

from blinkt import set_pixel, set_brightness, show, clear, set_all

def win(mapy, y, x):
    b1, b2, b3, b4, b5, b6, b7, b8 = True, True, True, True, True, True, True, True
    t1, t2, t3, t4 = 1, 1, 1, 1
    
    for i in range(1, 4):
        if x + i < len(mapy[0]) and y + i < len(mapy) and b1:
            # /
            if mapy[y+i][x+i] == mapy[y][x]:
                t1 += 1
            else: 
                b1 = False
        else:
            b1 = False
        
        if x - i >= 0 and y - i >= 0 and b2:
            # /
            if mapy[y-i][x-i] == mapy[y][x]:
                t1 += 1
            else:
                b2 = False
        else:
            b2 = False

        if x + i < len(mapy[0]) and y - i >= 0 and b3:
            # \
            if mapy[y-i][x+i] == mapy[y][x]:
                t2 += 1
            else:
                b3 = False
        else:
            b3 = False
        if x - i >= 0 and y + i < len(mapy) and b4:
            # \
            if mapy[y+i][x-i] == mapy[y][x]:
                t2 += 1
            else:
                b4 = False
        else:
            b4 = False

        if x - i >= 0 and b5:
            # -
            if mapy[y][x-i] == mapy[y][x]:
                t3 += 1
            else:
                b5 = False
        else:
            b5 = False
        if x + i < len(mapy[0]) and b6:
            # -
            if mapy[y][x+i] == mapy[y][x]:
                t3 += 1
            else:
                b6 = False
        else:
            b6 = False

        if y - i >= 0 and b7:
            # |
            if mapy[y-i][x] == mapy[y][x]:
                t4 += 1
            else:
                b7 = False
        else:
            b7 = False
        if y + i < len(mapy) and b8:
            # |
            if mapy[y+i][x] == mapy[y][x]:
                t4 += 1
            else:
                b8 = False
        else:
            b8 = False

    if t1 >= 4 or t2 >= 4 or t3 >= 4 or t4 >= 4:
        return True
    return False

def printmap(mapy, p1, p2, turn, index):
    cmd('clear')
    print('')
    print('\t', end='')

    end = False

    if turn:
        print(index*'    ', end='')
        print(f'{p1[0]}{p1[1]}███')
    else:
        print(index*'    ', end='')
        print(f'{p2[0]}{p2[1]}███')        
    print('')
    for smap in mapy:
        print('\t', end='')
        for e in smap:
            if e == 0:
                print(f"{Fore.WHITE}{Back.WHITE}██ {Style.RESET_ALL}", end=' ')
            elif e == 1:
                print(f"{p1[0]}{p1[1]}██ {Style.RESET_ALL}", end=' ')
            else:
                print(f"{p2[0]}{p2[1]}██ {Style.RESET_ALL}", end=' ')
        print('\n')
        
    ch = getch()
    if ch == '\t':
        index = index + 1
        if index > 7:
            index = 0
    elif ch == '\n':
        for i in range(8)[::-1]:
            if mapy[i][index] == 0:
                if turn:
                    mapy[i][index] = 1
                    end = win(mapy, i, index)
                    index = -1
                    break
                else:
                    mapy[i][index] = 2
                    end = win(mapy, i, index)
                    index = -1
                    break
        
    return index, mapy, end
    
def printmenu(sel, i1, i2):
    cmd('clear')
    
    colors = [[255, 0, 0], [238, 255, 0], [0, 255, 0], [0, 0, 255], [0, 255, 255], [238, 0, 255]]
    
    set_brightness(0.1)
    if sel == 2:
        set_all(255,255,255)
    elif sel == 0:
        set_all(colors[i1][0],colors[i1][1],colors[i1][2])
    else:
        set_all(colors[i2][0],colors[i2][1],colors[i2][2])
    show()
    
    print(f"\n\t{Fore.CYAN}{Style.DIM}{Style.BRIGHT}Welcome to duoBlinkt4\n{Style.RESET_ALL}")
    
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    backs = [Back.RED, Back.YELLOW, Back.GREEN, Back.BLUE, Back.CYAN, Back.MAGENTA]
    
    if sel == 0:
        print(f"\t{Style.BRIGHT}{colors[i1]}Player one{Style.RESET_ALL}		{colors[i2]}Player two{Style.RESET_ALL}")
        for i in range(7):
            print(f"\t{Style.BRIGHT}{colors[i1]}██████████{Style.RESET_ALL}		{colors[i2]}██████████{Style.RESET_ALL}")
        print('')
        print(f"\t{Fore.WHITE}{Style.DIM}             CONTINUE{Style.RESET_ALL}")
        print('')
    elif sel == 1:
        print(f"\t{colors[i1]}Player one{Style.RESET_ALL}		{Style.BRIGHT}{colors[i2]}Player two{Style.RESET_ALL}")
        for i in range(7):
            print(f"\t{colors[i1]}██████████{Style.RESET_ALL}		{Style.BRIGHT}{colors[i2]}██████████{Style.RESET_ALL}")
        print('')
        print(f"\t{Fore.WHITE}{Style.DIM}             CONTINUE{Style.RESET_ALL}")
        print('')
    else:
        print(f"\t{colors[i1]}Player one{Style.RESET_ALL}		{colors[i2]}Player two{Style.RESET_ALL}")
        for i in range(7):
            print(f"\t{colors[i1]}██████████{Style.RESET_ALL}		{colors[i2]}██████████{Style.RESET_ALL}")
        print('')
        print(f"\t{Style.BRIGHT}{Fore.WHITE}{Style.DIM}             CONTINUE{Style.RESET_ALL}")
        print('')
    
    status = False
    
    choice = getch()
    if choice == '\n':
        if sel == 0:
            i1 = i1 + 1
            if i1 > len(colors) - 1:
                i1 = 0
            if i1 == i2:
                i1 = i1 + 1
            if i1 > len(colors) - 1:
                i1 = 0
        elif sel == 1:
            i2 = i2 + 1
            if i2 > len(colors) - 1:
                i2 = 0
            if i1 == i2:
                i2 = i2 + 1
            if i2 > len(colors) - 1:
                i2 = 0
        else:
            status = True
    elif choice == '\x1b':
        pass
    elif choice == '\t':
        sel = sel + 1
        if sel > 2:
            sel = 0
        
    return sel, i1, i2, status
        
def play():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    backs = [Back.RED, Back.YELLOW, Back.GREEN, Back.BLUE, Back.CYAN, Back.MAGENTA]
    
    ok = False
    sel = 0
    p1 = 0
    p2 = 1
    while not ok:
        sel, p1, p2, ok = printmenu(sel, p1, p2)
    
    turn = True
    game = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
    
    cmd('clear')
    index = 0
    while 1:
        index, game, end = printmap(game, [colors[p1], backs[p1]], [colors[p2], backs[p2]], turn, index)
        if end:
            cmd('clear')

            if turn:
                print('player 1 won')
            else:
                print('player 2 won')

            getch()
            break
        if index == -1:
            turn = not turn
            index = 0
        
    
    cmd('clear')
