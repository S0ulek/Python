weather = int(input("Сколько градусов на улице: "))
dist = 0
while weather>15:
    dist += 20
    weather -= 2
    if weather <= 15:
        print("Слишком холодно")
        break       
    dist += 10
print("Пройденное расстояние:",dist)