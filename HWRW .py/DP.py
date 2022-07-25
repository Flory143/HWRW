import os
import webbrowser
from os import system

print('Help With Reinstall Windows by Foxxer, ver.1.0.0')

def start_menu():
    print('------------------------------------------')
    print('1. Скачать Windows.iso')
    print('2. ')
    print('3. 3')
    print('Выйти - Exit')
    print('------------------------------------------')

    start = input('Ваш выбор >> ')

    system('cls') 
    if start == 'Exit':
        exit()   
    elif start == '1':
        download_windows()
    elif start == '5':
        chrome()
    else:
        pass

def chrome():
    choice = input('Нажмите установить > откройте скаченный файл и следуйте инструкции! ENTER')
    if choice == '':
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/ChromeSetup.exe', new=2)
        system('cls')
        start_menu()

def download_windows():
    print('Выберите одну из списка: ')
    print('1. Windows 10')
    print('2. Windows 11 (in next update)')
    choice = input('Ваш выбор >> ')
start_menu()