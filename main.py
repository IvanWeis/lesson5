import os
import shutil
import bank_account
from borndayforever import check_year, check_day
# из модуля borndayforever импортируем функцию проверки года рождения и дня рождения

while True:
    print()                        # печатаем пустую строку (для удобства восприятия)
    print(' 0.определить путь рабочей директории')
    print(' 1.создать папку')
    print(' 2.удалить папку')
    print(' 3.копировать файл')
    print(' 4.просмотр содержимого рабочей директории')
    print(' 5.посмотреть только папки')
    print(' 6.посмотреть только файлы')
    print(' 7.просмотр информации об операционной системе')
    print(' 8.создатель программы')
    print(' 9.играть в викторину')
    print('10.мой банковский счет')
    print('11.выход')

    choice = input('Выберите пункт меню: ')
    if choice == '0':
        print("Текущая деректория:", os.getcwd())
    elif choice == '1':
        name = input("Введите имя создаваемой папки: ")
        if not os.path.exists(name):
            os.mkdir(name) # создать папку в текущей папке, если такой нет
    elif choice == '2':
        name = input("Введите имя удаляемой папки: ")
        if os.path.exists(name):
            os.rmdir(name)     # удалить папку в текущей папке, если такая есть
    elif choice == '3':
        name = input("Введите имя копируемого файла: ")
        name_copy = input("Введите имя файла-копии: ")
        shutil.copy(name, name_copy)      # копировать файл или папку
    elif choice == '4':
        print("Все папки и файлы:", os.listdir())  # просмотр содержимого рабочей директории (напечатать)
    elif choice == '5':      # посмотреть только папки
        for dirpath, dirnames, filenames in os.walk("."):
            for dirname in dirnames:
                 print("Каталог:", os.path.join(dirpath, dirname))
    elif choice == '6':      # посмотреть только файлы
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                 print("Файл:", os.path.join(dirpath, filename))
    elif choice == '7':
        print(os.name)      # информация об операционной системе
    elif choice == '8':
        print("Вайс И.А.")   # печатаем создателя программы
    elif choice == '9':
        check_year()         # вызываем функцию проверки года рождения
        check_day()          # вызываем функцию проверки дня рождения
    elif choice == '10':
        bank_account.bank()   # вызываем функцию bank(), содержащуюся в модуле bank_account.py
    elif choice == '11':
        break                # выход из программы
    else:
        print('Неверный пункт меню')
