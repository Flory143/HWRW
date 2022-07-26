import os
import webbrowser
from os import system
import igpu

system('cls')
version = '1.0.0'

def start_menu():
    print('Version - ' + version)
    print('Help With Reinstall Windows by Foxxer')
    print('-----------------------------------------------------')
    print('1. Скачать Windows.iso')
    print('2. Скачать Rufus')
    print('3. Скачать Chrome')
    print('4. Nvidia/Amd драйвера для видеокарты (если имеется)')
    print('5. Программы')
    print('6. Помощь')
    print()
    print('Выйти - Enter')
    print('-----------------------------------------------------')

    choice = input('Ваш выбор >> ')

    system('cls') 
    if choice == '1':
        download_windows()
    elif choice == '2':
        rufus()
    elif choice == '3':
        chrome()
    elif choice == '4':
        drivers()
    elif choice == '5':
        programs()
    elif choice == '6':
        help()
    else:
        pass


def download_windows():
    print('!!! Внимание !!! ДЛЯ УСТАНОВКИ ТРЕБУЕТСЯ TORRENT КЛИЕНТ !!! (3)')
    print('Выберите одну из списка: ')
    print()
    print('1. Windows 10')
    print('2. Windows 11 (Скоро)')
    print('3. Скачать qBittorrent')
    print()
    print('Назад - ENTER')
    print()
    
    choice = input('Ваш выбор >> ')

    if choice == '1':
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/Windows/Windows10ruPRO-HOME.torrent', new=2)
    elif choice == '2':
        system('cls')
        download_windows()
    elif choice == '3':
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/qbittorrent_4.4.3.1_x64_setup.exe', new=2)
    else:
        system('cls')
        start_menu()

def rufus():
    print('Rufus — бесплатное портативное приложение с открытым исходным кодом для Microsoft Windows, которое можно использовать для форматирования и создания загрузочных USB-накопителей.')
    print()
    choice = input('Скачать Rufus - ENTER')
    webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/rufus-3.19p.exe')
    system('cls')
    start_menu()

def chrome():
    choice = input('Нажмите установить > откройте скаченный файл и следуйте инструкции! - ENTER')
    if choice == '':
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/ChromeSetup.exe', new=2)
        system('cls')
        start_menu()

def drivers():
    gpu = igpu.get_device(0)
    print(f'Ваша видео карта - ' + gpu.name)
    gpu_name = gpu.name
    NVIDIA = 'NVIDIA'
    AMD = 'AMD'
    if NVIDIA in gpu_name:
        print()
        choice = input('Перейти на сайт производителя. - ENTER ')
        webbrowser.open('https://www.nvidia.com/ru-ru/geforce/drivers/')
        system('cls')
        start_menu()
    elif AMD in gpu_name:
        print()
        choice = input('Перейти на сайт производителя. - ENTER ')
        webbrowser.open('https://www.amd.com/ru/support')
        system('cls')
        start_menu()

def programs():
    print('Записывайте без запятых и пробелов!')
    print()
    print('1. GHub')
    print('2. 7-ZIP')
    print('3. Steam')
    print('4. VSCode')
    print('5. Discord')
    print('6. Telegram')
    print()
    print('Назад - ENTER')
    print()

    choice = input('Ваш выбор >> ')

    if '1' in choice:
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/lghub_installer.exe')
    if '2' in choice:
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/7z-x64.exe')
    if '3' in choice:
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/SteamSetup.exe')
    if '4' in choice:
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/VSCodeSetup-x64.exe')
    if '5' in choice:
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/DiscordSetup.exe')
    if '6' in choice:
        webbrowser.open('https://github.com/Flory143/HWRW/raw/main/Programs/tsetup-x64.exe')
    else:
        pass

    system('cls')
    start_menu()


def help():
    print('Скоро')

start_menu()