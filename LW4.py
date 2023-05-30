def z1():
    res = None
    try:
        chislo = int(input("введите число:      "))
        delit = chislo % 3
    except ValueError:
        print("вы ввели не число, повторите ввод")
    else:
        if delit == 0 and chislo != 0:
            print("число", chislo, "делится на 3")
        elif chislo == 0:
            print("введён ноль")
        else:
            print("число", chislo, "не делится на 3 :(  ")

def z2():)
    try:
        chislo = int(input("введите число:     "))
        delit = 100 / chislo
    except ZeroDivisionError:
        print("вы ввели 0")
    except ValueError:
        print("вы ввели не число, повторите ввод")
    else:
        print("результат деления - ", delit)

def z3():
    date = input("введите дату в формате дд.мм.гггг:     ")
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print("поздравляю, дата магическая")
    else:
        print("дата не является магической, попробуйте заново :(  ")
def z4():
    ticket = input("введите номер билета:    ")
    schet1 = 0
    chet2 = 0
    if len(ticket) % 2 == 0:
        for i in ticket[0:int(len(ticket) / 2)]:
            schet1 = schet1 + int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket)) + 1]:
            chet2 = chet2 + int(i)
        if schet1 == chet2:
            print("вы приобрели счастливый билет, ура")
        else:
            print("билет не является счастливым :(( ")
    else:
        print("количество цифр нечётно, купите новый билет")

z1()
z2()
z3()
z4()