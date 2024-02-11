positive = 0
negative = 0
while True:
    rate = int(input("Введите число:"))
    if rate > 0:
        positive += 1
    elif rate <0:
        negative += 1
    else:
     print("Кол-во положительных чисел:",positive, "\nКол-во отрицательных чисел:",negative)
     break