from colorama import init as colorama_init
from colorama import Fore, Back, Style
from os import system as cmd
from getch import getch

from blinkt import set_pixel, set_brightness, show, clear, set_all

def win(mapy, y, x):
    # horizontal
    tr = True, tl = True
    r = 0, l = 0
    for in range(3):
        if mapy[y][x + 1] == mapy[y][x] and tr:
            r += 1
        else:
            tr = False
        if mapy[y][x - 1] == mapy[y][x] and tl:
            l += 1
        else:
            tl = False
    # vertcal
    tt = True, tb = True
    t = 0, b = 0
    for in range(3):
        if mapy[y + 1][x] == mapy[y][x] and tt:
            t += 1
        else:
            tt = False
        if mapy[y - 1][x] == mapy[y][x] and tb:
            b += 1
        else:
            tb = False
    # dep
    ttl = True, tbr = True
    tl = 0, br = 0
    for in range(3):
        if mapy[y + 1][x] == mapy[y][x] and tt:
            t += 1
        else:
            tt = False
        if mapy[y - 1][x] == mapy[y][x] and tb:
            b += 1
        else:
            tb = False

def printmap(mapy, p1, p2, turn, index):
    cmd('clear')
    print('')
    print('\t', end='')
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
                    mapy[i][index] = 1;
                    index = -1
                    if win(mapy, i, index):
                        ...
                    break
                else:
                    mapy[i][index] = 2;
                    index = -1
                    if win(mapy, i, index):
                        ...
                    break
        
    return index, mapy 
    
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
    end = False
    while not end:
        index, game = printmap(game, [colors[p1], backs[p1]], [colors[p2], backs[p2]], turn, index)
        if index == -1:
            turn = not turn
            index = 0
    
    cmd('clear')
