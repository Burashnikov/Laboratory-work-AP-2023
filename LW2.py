def z1():
    pw1 = input('Введите пароль: ') #ввод пароля
    pw2 = input('Повторите пароль: ') #повторный ввод
    if pw1 == pw2: #если пароли совпадают, то выводит сообщение, что пароль принят
        print('Пароль принят')
    else: #если не совпадают, то выводит, что не принят
        print('Пароль не принят')

def z2():

    number = int(input('Введите номер вашего места: ')) #ввод номера

    if number > 36 and number < 55: #если номер находится в промежутке между 36 и 55, то место боковое
        print('Ваше место - боковое')
    elif number < 36 and number > 0: #если номер находится в промежутке между 0 и 36, то купе
        print('Ваше место - купе')

    if number % 2 == 0 and number > 0 and number < 55: #если число из промежутка 0 до 55 делится без остатка, то место верхнее
        print('Ваше место - верхнее')
    elif number % 2 == 1 and number > 0 and number < 55: #если число из промежутка 0 до 55 делится с остатком, то место нижнее
        print('Ваше место - нижнее')

def z3():

    year = (int(input('Введите год: ')))  #ввод года

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #проверяем год, чтоб делился на 4 и на 400 без остатка, но чтоб не делился на 100
        print(year, 'Год високосный') #если все условия выполнены, то выводит, что год високосный
    else:
        print(year, 'Год не високосный') #если не выполняется, то выводит что нет

def z4():

    Color1 = input('Введите первый цвет: ') #ввод цвета
    Color2 = input('Введите второй цвет: ') #ввод цвета

    if Color1 != "Красный" and Color1 != "Синий" and Color1 != "Желтый": #если вводим не основные, то выводим ошибку
        print('Ошибка')
    if Color2 != "Красный" and Color2 != "Синий" and Color2 != "Желтый":
        print('Ошибка')

    if Color1 == 'Красный' and Color2 == 'Синий': #перебираем варианты цветов и выводим, что в итоге получится
        print('Получится - Фиолетовый')
    if Color1 == 'Синий' and Color2 == 'Красный':
        print('Получится - Фиолетовый')
    if Color1 == 'Красный' and Color2 == 'Желтый':
        print('Получится - Оранжевый')
    if Color1 == 'Желтый' and Color2 == 'Красный':
        print('Получится - Оранжевый')
    if Color1 == 'Синий' and Color2 == 'Желтый':
        print('Получится - Зелёный')
    if Color1 == 'Желтый' and Color2 == 'Синий':
        print('Получится - Зелёный')

z1(),z2(),z3(),z4()