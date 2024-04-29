import math

def sphere_area(radius):
    print(4 * math.pi * radius ** 2)


def sphere_volume(radius):
    print(4 / 3 * math.pi * radius ** 3)


radius_of_planet = float(input("Введите радиус планеты: "))
sphere_area(radius_of_planet)
sphere_volume(radius_of_planet)
