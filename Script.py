#!/usr/bin/python3

import os
def clear():
    os.system('cls||clear')

def user():
    clear()
    if os.geteuid() != 0:
        exit('Please run the script with Sudo Permissions\nExiting...')
    Loop = 0
    while Loop != 1:
        clear()
        print('''Do you want to install Devon's Program Script?''')
        Anws = input('')
        if Anws == 'y' or Anws == 'yes':
            clear()
            print('Ok Installing :)')
            #install()
            Loop = 1
#def install():
    #os.popen('')
    
user()