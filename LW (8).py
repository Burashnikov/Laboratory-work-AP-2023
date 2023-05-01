from PIL import Image, ImageDraw

def z1():
    p = "picone.jpg"
    with Image.open(p) as img: #открывает изображение
        img.load() #считывает изображение
        img.show() #открывает изображение
        cropp_img = img.crop((100, 100, 100, 100)) #обрезка изображения
        cropp_img.save("piconenew.jpg") #сохраняет новое изобажение

def z2():
    g = {1: "NG.jpeg", 2: "march.jpg", 3: "february.jpg", 4: "prazdnik.jpeg"} #создаем словарь где каждому номеру соответсвует праздник

    print("1-НГ"
          "2-8 марта"
          "3-23 февраля"
          "4-др")
    ans = int(input("Выберите цифру, соответсвующую празднику: ")) #выводим и просим выбрать цифру

    p = g[ans] #в результате того что выбрали выводит необходимую открытку
    with Image.open(p) as img:
        img.load()
        img.show()

def z3():
    p = "prazdnik.jpeg"
    with Image.open(p) as img:
        img.load()

    txt = ImageDraw.Draw(p) #модуль который рисует текст на открытке
    ans = int(input("Введите имя человека: ")) #ввод кому открытка адресована
    txt.text((100, 100), ans, ", поздравляю!", fill = ("black")) #параметры текста: значение и заливка

    p.save("postcard.jpg") #сохранение новой открытки

z1(), z2(), z3()

