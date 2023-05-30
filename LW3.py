def zadanie1():

    words = []
    while (word := str(input())) != "stop":
        words.append(word)
    print("".join(words))

def zadanie2():
    words2=[]
    while (newword := str(input())) != "stop":
        if "ф" in newword or "Ф" in newword:
            print("это редкое слово!")
        else:
            print("это обычное слово")

def zadanie3():
    from random import randint
    wrong = 0
    right = 0
    print("для завершения игры напишите stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f" {a} + {b} =  ", end = "")
        res = input()
        while not res.isdigit() and res != "stop":
            print("при вводе допущена ошибка, повторите ввод", end = "")
            res = input()
        if res == "stop":
            break
        res = int(res)
        if a+b == res:
            right +=1
            print("правильно")
        else:
            wrong +=1
            print("неправильно")
        if wrong == 3 :
            print("игра окончена, правильных ответов", right)


zadanie1(), zadanie2(), zadanie3()