import random
from random import randint
def z1():
    print("Первое задание")
    a = 5
    list = [] #создаю список из 5 рандом чисел (рандом из библиотеки питон)
    for i in range(a):
        item = randint(1,99)
        list.append(item)
    n = int(input("введите число "))
    if n in list:
        print("Поздравляю, вы угадали число", *list)
    else:
        print("нет такого числа", *list)




from random import randint
def z2():
    print("Задание два")
    b = 5
    list = [] #тоже список из 5 рандом числе
    for i in range(b):
        item = randint(1,99)
        list.append(item)
    print(*filter(lambda x : list.count(x) > 1, list)) #если в списке есть элемент повторяющийся более одного раза, список выводится

def z3():
    print("Задание три")
    ned = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс") #кортеж с днями недели
    d = int(input("сколько выходных? "))
    for i in ned:
        print("Рабочие", *ned[:-d]) #вывод рабочих дней и следом выходных
        print("Выходные", *ned[-d:])
        break

from random import sample
def z4():
    print("Задание четыре")
    list =["Бурашников" , "Суворов" , "Андреев"]
    list2 = ["Чернейкина", "Троицкая" , "Бурашникова"]
    team = tuple(random.sample(list,2)+random.sample(list2,2)) #объединяем группы
    print(*list) #исходный
    print(*list2)
    print(*team) #новый
    print(len(team)) #длина
    team = tuple(sorted(team))
    if "Иванов" in team: #проверка Иванова
         print(team).count("Иванов")
    else:
        print("нет")


z1(), z2(), z3(), z4()