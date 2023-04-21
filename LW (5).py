def z51():
    import random

    chisla = []
    for i in range(5):
        chisla.append(random.randint(0,100))
    n =  int(input("Введите число"))
    if n in chisla:
        print("вы угадали!")
    else:
        print("такого числа нет")

    print("Вот ваш список ", *chisla)

def z52():

    import random

    from collections import counter

    chisla = []
    for i in range(5):
        chisla.append(random.randint(0, 100))
    counter = counter(chisla)
    print(counter)

z51(), z52()
