import time
import random

A = input("Do you want to enter? (yes/no): ")

if A != "yes":
    quit()

time.sleep(2)

while True:
    print("""
    █▀█ ▄▀█ █▀ █▀ █░█░█ █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
    █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
    """)
    time.sleep(2)
    print("created by M4NANONYM")
    time.sleep(2)

    length = int(input("How many characters do you want the password to be long (write in number)? "))
    time.sleep(2)
    print("creating password...")

    letters = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    numbers_symbols = "0123456789;,:._-!()[]{}"
    P = letters + numbers_symbols
    time.sleep(2)
    password = "".join(random.sample(P, length))
    print("Password: ", password)
    input("Press enter to generate other password")



