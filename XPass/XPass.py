import time
import secrets
import string
import re
from colorama import Fore, Style
import random
import os
import subprocess
import base64

# that's still a work in progress (will be used to create random file names) <- not likely
def generate_random_name(length):
    letters = string.ascii_lowercase
    rname = ''.join(random.choice(letters) for i in range(length))
    return rname



def xpass() :
    checkinput = input(Fore.MAGENTA + "----------------------------------\nCheck your password for data breaches: \n->" + Style.RESET_ALL)
    with open('breach.txt', 'r') as f:
        for line in f.readlines():
            if line.startswith(checkinput):
                print (Fore.GREEN + checkinput + Fore.MAGENTA + " was found in our database, the password is " + status + " . We recommend to change it." + Fore.MAGENTA + "\n------------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
            else:
                check_pass = re.compile(r'''(
                        ^.*(?=.{10,})           
                        (?=.*d)                
                        (?=.*[a-z])             
                        (?=.*[A-Z])             
                        (?=.*[@#$%^&+=!]).*$    
                        )''', re.VERBOSE)

                mo1 = check_pass.search(checkinput)

                if mo1:
                    status = (Fore.GREEN + "strong")
                else:
                    status = (Fore.RED + "weak")

                print(Fore.GREEN + checkinput + Fore.MAGENTA + " was not found in our database, the password is " + status + Fore.MAGENTA + "\n------------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
                time.sleep(5)
    
    input("->")
    menu()

def generator():
    print(Fore.MAGENTA + "_______________________________________________\nXPass Generator " + version + "\n_______________________________________________" + Style.RESET_ALL)
    #genver = input(Fore.MAGENTA + "Which type of generator would you like to use :\n[1] - Random characters(hard to remember, extreme hard to hack)\n[2] - Random words (easy to remember, hard to hack)\n" + Style.RESET_ALL)
    pwd_length = int(input(Fore.MAGENTA + 'How many chars would you like to be in your password?\n' + Style.RESET_ALL))
    time.sleep(2)
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    print(Fore.LIGHTGREEN_EX + "Generated password is : " + pwd + Style.RESET_ALL)
    input("Press enter to proceed...")
    menu()


# currently onto this thingy under this line
# not working list : saving multiple passwords
def keychain():
    print("Welcome to XPass keychain [beta]")
    choice = input("Menu:\n[1] - Add a new password\n[2] - View your passwords\n[3] - Exit to the XPass\n-> ")
    if choice == '1':
        userinput = input("Enter a website for password that you would like to add: ")
        userinput2 = base64.b64encode(bytes(userinput, 'utf-8'))
        passinput = input("Enter password that will be saved and attached to the last input: ")
        passinput2 = base64.b64encode(bytes(passinput, 'utf-8'))
        with open('vvvrqo.txt', 'a') as f:                                 # with open(f'{here goes variable for random file mame}.txt', 'a') as f:
            f.write(f'{userinput}:{passinput}\n')                                       # that comment is for a random filename(next feature)
            subprocess.check_call(["attrib","+H","vvvrqo.txt"])
        
        keychain()
    if choice == '2':
        with open('vvvrqo.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                username = parts[0]
                username2 = base64.b64decode(bytes(username, 'utf-8'))
                passkey = parts[1]
                passkey2 = base64.b64decode(bytes(passkey, 'utf-8'))
                print(f"Website: {username}, password: {passkey}")
                input("Press any key to proceed")
                keychain()
                

def check():
    if not os.path.exists('lielvv.txt'):
        apppass = input("lielvv.txt not found\nEnter a password that will be needed every time you open the app(for security): ")
        with open('lielvv.txt', 'w') as f:
                f.write(f'{apppass}')
        print("Operation completed.")

    with open('lielvv.txt', 'r') as f:
        apppass = f.read()
        inputpass = input("Enter password to access the app: ")
        if inputpass == apppass:
            menu()
        else:
            exit('Access denied')



def menu():
    asciitext = " _     _  _____  _______ _______ _______\n  \___/  |_____] |_____| |______ |______\n _/   \_ |       |     | ______| ______|"
    print(Fore.MAGENTA + asciitext + Style.RESET_ALL)
    print(Fore.MAGENTA + "version " + version + Style.RESET_ALL)
    gen = input(Fore.MAGENTA + '_________________________\n|                       |\n|Select an option       |\n|[1] - XPass            |\n|[2] - XPass Generator  |\n|[3] - XPass Keychain   |\n|[4] - Exit             |\n|_______________________|\n-> ' + Style.RESET_ALL)
    if gen == '1':
        xpass()
    if gen == '2':
        generator()
    if gen == '3':
        keychain()
    if gen == '4':
        exit()
    else:
        print('input is invalid')
        menu()

version = ("2.0") # im a sonic fan =)


check()
menu()
