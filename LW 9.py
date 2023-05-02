import os
from PIL import Image
import csv

def z1():
    input_folder = "C:\Users\My PC\Desktop\LW\LW (9)\input" #начальная папка
    output_folder = "C:\Users\My PC\Desktop\LW\LW (9)\output" #папка с обработкой

    for filename in os.listdir(input_folder):
        #если файл - изображение, то берет его из начальной папки
        if filename.endswith(".jpg"):
            with Image.open(os.path.join(input_folder, filename)) as img:
                new_img = img.transpose(Image.ROTATE_180) #проводит обработку - поворот на 180 градусов
                new_img.save(os.path.join(output_folder, filename)) #закидывает в папку с обработкой


def z2():
    input = "C:\Users\My PC\Desktop\LW\LW (9)\input"
    output = "C:\Users\My PC\Desktop\LW\LW (9)\output"
    for filename in os.listdir(input):
        if filename.endswith(".jpg") or filename.endswith(".png"): #проводит обработку только тем файлам которые соответствуют необходимым формата
            with Image.open(os.path.join(input, filename)) as img:
                new_img = img.transpose(Image.ROTATE_180)
                new_img.save(os.path.join(output, filename)) #сохраняет в папку с обработкой


def z3():
    filename = "data.csv"
    data = {}

    with open(filename, "r") as file:
        reader = csv.reader(file) #читаем csv файл с помощью reader(интегрирует csv файл построчно)
        next(reader)
        for row in reader:
            #привызяываем значения
            product = row[0] #продукты
            quantity = int(row[1]) #количество
            price = int(row[2]) #цена
            data[product] = {"quantity": quantity, "price": price}

    total_cost = sum(data[product]["quantity"] * data[product]["price"] for product in data) #подсчет итоговой суммы

    print("Нужно купить:")
    for product in data:
        quantity = data[product]["quantity"] #считывает количество
        price = data[product]["price"] #цену
        print(f"{product} - {quantity} шт. за {price} руб.") #вывод необходимого
    print(f"Итоговая сумма: {total_cost} руб.") #вывод итоговой суммы

z1(), z2(), z3()