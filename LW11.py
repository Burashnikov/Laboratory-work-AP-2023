def z1():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):     #задаем аргументы для класса
            self.restaurant_name = restaurant_name  #self имя класса
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name}, кухня - {self.cuisine_type}.")
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant("Кореана","Корейская")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant() #


def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name}, кухня - {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    restaurant1 = Restaurant("Кореана", "Корейская")
    restaurant2 = Restaurant("Токио", "Японская")
    restaurant3 = Restaurant("Хинкальня", "Грузинская")


    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def z3():
        print("Задание 3")
        class Restaurant:
            def __init__(self, restaurant_name, cuisine_type, rating_restaurant):
                self.restaurant_name = restaurant_name
                self.cuisine_type = cuisine_type
                self.rating_restaurant = rating_restaurant

            def describe_restaurant(self):
                print(f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type} Грузинская, рейтинг ресторана: {self.rating_restaurant}')

            def open_restoraunrt(self):
                print('Ресторан сейчас открыт')

            def rrating_restaurant(self):
                print(f'Новый рейтинг ресторана: {input("Введите новый рейтинг: ")}')

        new_Restaurant = Restaurant('Хинкальня', '', 5)
        new_Restaurant.describe_restaurant()
        new_Restaurant.open_restoraunrt()
        new_Restaurant.rrating_restaurant()
z1()
z2()
z3()