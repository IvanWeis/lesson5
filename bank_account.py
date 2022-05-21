# ОПРЕДЕЛЕНИЯ ПЕРЕМЕННЫХ И ФУНКЦИИ
def bank():
    remains = 0  # обнуляем остаток денег на счету
    kwargs = {}  # в данном словаре храним историю покупок
    #naimen = " "
    while True:
        print()                        # печатаем пустую строку (для удобства восприятия)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            print("У Вас на счету: ", remains)
            remains = remains + int(input("Введите сумму пополнения счета: "))
            print("У Вас на счету: ", remains)
        elif choice == '2':
            spisok = input("Введите через пробел Наименование и Сумму покупки: ") # вводим строку из 2-х элементов
            spisok = spisok.split(" ")  # разбиваем строку на 2 элемента массива через пробел
            naimen = spisok[0]  # вытаскиваем первый элемент списка (Наименование)
            summa = int(spisok[1]) # вытаскиваем второй элемент списка (Сумма)
            if remains - summa < 0:  # если остаток на счете меньше суммы покупки
                print("Не хватает денег. Пополните счет")
            else:                    # если денег на счете хватает для осуществления покупки
                #remains = top_up(remains)     # уменьшение счета
                remains = remains - summa  # уменьшаем остаток на сумму покупки
                print("Покупка произведена. Остаток денег на Счете: ", remains)
                #kwargs = purchases_history()  # формирование истории покупок
                kwargs[naimen] = summa  # добавляем строку в историю покупок
                print(kwargs)
        elif choice == '3':
            print("История Ваших покупок: ")  # вывод истории покупок
            print(kwargs)
        elif choice == '4':
            break                             # выход из программы
        else:
            print('Неверный пункт меню')

# ИСПОЛНЯЕМАЯ ЧАСТЬ ПРОГРАММЫ:
if __name__ == '__main__':
     bank() # вызываемфункциюю bank()