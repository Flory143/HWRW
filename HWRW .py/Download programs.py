import os
from os import system
from colorama import Fore, Back, Style
from colorama import init
init()

def start_menu():
    print("------------------------------------------")
    print("1. Chrome")
    print("2. 2")
    print("3. 3")
    print("Выйти - Exit")
    print("------------------------------------------")

    start = input("Ваш выбор " + Back.GREEN + ">>" + Back.RESET + " ")

    system("cls") 
    if start == "Exit":
        exit()   
    elif start == '1':
        chrome()
    else:
        pass

def chrome():
    choice = input("Нажмите установить > откройте скаченный файл и следуйте инструкции! ENTER")
    if choice == "":
        os.system("vk.com")
        system("cls")
        start_menu()

start_menu()