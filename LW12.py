def z1():
    class Restaurant:
        def __init__(self,restaurant_name):     #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name      #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant): #наследующий класс ресторант класс мороженое
        def __init__(self,restaurant_name,flavors): #создаем атрибуты вкус название
            self.restaurant_name = restaurant_name
            self.flavors = flavors
        def vivod_sortov(self):
            print("Сорта мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
    newIceCreamStand = IceCreamStand("Кафе-мороженное",["Ванильное", "Шоколадное","Фисташковое","Клубничное"])
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.vivod_sortov()


def z2():

    class Restaurant:
        def __init__(self,restaurant_name):
            self.restaurant_name = restaurant_name
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,adress,vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
        def opisanie(self):
            print("Местоположение: ", self.adress,"\nВремя работы: ", self.vremya_raboti)
        def vivod_sortov(self):
            print("Вкусы мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
        def add_flovor(self,flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлен в список вкусов.")
        def remove_flavor(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} былo удалено из списка вкусов.")
            else:
                print(f"{flavor} - такого вкуса нет в списке!")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} имеется в списке вкусов.")
            else:
                print(f"{flavor} НЕ имеется в списке вкусов.")
    newIceCreamStand = IceCreamStand("Кафе-мороженное","ст.м.Сенная Площадь, 21", "Ежедневно с 10:00 до 22:00")
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.opisanie()
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.add_flovor("Ванильное")
    newIceCreamStand.add_flovor("Шоколадное")
    newIceCreamStand.add_flovor(input("Какое ещё добавить? "))
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.remove_flavor(input("Какое удалить? "))
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.check_flavor(input("Какое мороженное проверить в наличии? "))
def z24():
    class Restaurant:
        def __init__(self,restaurant_name):
            self.restaurant_name = restaurant_name
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,adress,vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
        def opisanie(self):
            print("Местоположение: ", self.adress,"\nВремя работы: ", self.vremya_raboti)
        def vivod_sortov(self):
            print("Вкусы мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
        def add_flovor(self,flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлен в список вкусов.")
        def remove_flavor(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} былo удалено из списка вкусов.")
            else:
                print(f"{flavor} - такого вкуса нет в списке!")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} имеется в списке вкусов.")
            else:
                print(f"{flavor} НЕ имеется в списке вкусов.")
    class Palochka(IceCreamStand):
        def __init__(self, restaurant_name, adress, vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
            self.type = "Мороженное на палочке"
        def describe_type(self):
            print(f"Вид: {self.type}")
    class Rozhok(IceCreamStand):
        def __init__(self, restaurant_name, adress, vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
            self.type = "Мороженное в рожке"
        def describe_type(self):
            print(f"Вид: {self.type}")

    newIceCreamStand = IceCreamStand("Кафе-мороженное","ст.м.Сенная Площадь, 21", "Ежедневно с 10:00 до 22:00")
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.opisanie()
    newIceCreamStand = Palochka("Кафе-мороженное", "Мороженное77", "Морожка")
    new2IceCreamStand = Rozhok("Кафе-мороженное", "Мороженное77","Морожка")

    newIceCreamStand.add_flovor("Ванильное")
    newIceCreamStand.add_flovor("Шоколадное")

    new2IceCreamStand.add_flovor("Ягодное")
    new2IceCreamStand.add_flovor("Пломбир")

    newIceCreamStand.describe_type()
    newIceCreamStand.vivod_sortov()

    new2IceCreamStand.describe_type()
    new2IceCreamStand.vivod_sortov()


import tkinter as tk
def z3():
    class window:
        def __init__(self, flavors):
            self.flavors = flavors
            self.window = tk.Tk()
            self.label_title = tk.Label(self.window, text="Вкусы мороженого:")
            self.label_title.pack() #добавление заголовка в окно
            self.listbox_flavors = tk.Listbox(self.window)
            self.listbox_flavors.pack()

            for flavor in self.flavors:
                self.listbox_flavors.insert(tk.END, flavor)

        def run(self):
            self.window.mainloop()

    class IceCreamStand:
        def __init__(self, flavors):
            self.flavors = flavors

        def print(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

    flavors = ["Шоколад", "Ваниль", "Клубника", "Карамель"]

    iceCreamStand = IceCreamStand(flavors)
    iceCreamStand.print()

    show = window(flavors)
    show.run()


z1(), z2(), z24(), z3()