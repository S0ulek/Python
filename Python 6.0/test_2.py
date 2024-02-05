bags = int(input("Введите количество мешков:"))
weight = 0
while bags > 0:
    bag_weight = int(input("Вес мешка: "))
    weight += bag_weight
    bags -= 1
print("Общий вес мешком составил:", weight, "кг")