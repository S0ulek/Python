import math

volume_earth = 10.8321 * 10 ** 11
radius = float(input("Введите радиус случайно планеты:"))
volume_random_planet = (4/3) * math.pi * radius ** 3

if volume_earth > volume_random_planet:
    ratio = volume_earth / volume_random_planet
    print ("Объём планеты Земля больше в",round(ratio,3), "раз")
else:
    ratio = volume_random_planet / volume_earth
    print("Объём планеты Земля меньше в", round(ratio,3), "раз")
