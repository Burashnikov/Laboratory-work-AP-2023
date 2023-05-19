import json

def z1():
    with open('primer.json', 'r', encoding='utf-8') as f:
        file = json.load(f)  #содержимое файла в словарь

    for i in file['products']:
        print(f"Название: {i['name']}") #ключам присваиваем значения
        print(f"Цена: {i['price']}")
        print(f"Вес: {i['weight']}")
        if i['available'] == True:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z2():
    with open('primer.json', encoding='utf-8') as f:
        file = json.load(f)

    name = input("Введите название продукта: ")
    price = input("Введите цену продукта: ")
    weight = input("Введите вес продукта: ")
    available = input("Есть ли продукт в наличии?") == 'да'
    slovar = {"name": name, "price": price, "available": available, "weight": weight}
    file["products"].append(slovar) #добавление словаря в нач список
    with open('primer.json', 'w', encoding='utf-8') as f:
        json.dump(file, f)  #список сверху
    print()
    print()

    with open('primer.json') as f:
        file = json.load(f)
        for i in file['products']:
            print(f"Название: {i['name']}")
            print(f"Цена: {i['price']}")
            print(f"Вес: {i['weight']}")
            if i['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print()

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as fi:
        spisok = fi.readlines() #список в строку
        print(spisok)
    ru_en = {}
    for i in spisok:
        e, r = i.strip().split(' - ')
        for rusword in r.split(','):
            ru_en.setdefault(rusword.strip(), []).append(e.strip()) # setdefault -> ключ русский - ему англ в соответствие

    sort_slovar = dict(sorted(ru_en.items()))
    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word, en_words in sort_slovar.items():
            f.write(f"{ru_word} - {', '.join(en_words)}\n") #перезапись итогового файла

z1()
z2()
z3()


