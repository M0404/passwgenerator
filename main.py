import colorama
import time
import random
from colorama import Fore, Back, Style

lis = "Yy"
dom = input("Do you want to continue (Y/n)?: ")
if dom.upper() in lis.upper():
    print("")
else:
    quit()
colorama.init()
print(Fore.CYAN + '''
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
''')
time.sleep(2)
print(f"{Fore.LIGHTYELLOW_EX}{Style.NORMAL} CREATED BY M404")

ele = Fore.MAGENTA + """

[1] Generate a password

[2] Exit    
"""
print(ele)
cho = input("Choice: ")
repeat = True
while (repeat):
    if cho == "1":
        lett = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
        nu = "0123456789"
        sym = "{}_-|!/%=&[]"

        all = lett + nu + sym
        lun = int(input("Length of the password: "))
        time.sleep(2)
        passw = "".join(random.sample(all,lun))
        print("Password: ", passw)
        time.sleep(2)
    elif cho == "2":
        quit()
    else:
        quit()


    poss_ris = "Yy"
    ans = input("Do you want to generate another password (Y/n)?: ")
    if ans.upper() in poss_ris.upper():
        print("")
    else:
        print("bye!!!")
        repeat = False
