import math


def about_water(price):
    print("Название: КлирВотер\n"
          "Производитель: ВодЗавод\n"
          f"Цена: {price}")


for _ in range(3):
    price_of_water = int(input("Введите цену "))
    about_water(price_of_water)

