reverse_timer = 60
for interval in range (reverse_timer,0, -5):
    print("Осталось", interval,"секунд.")
    check = int(input("Вы хотите остановить разогрев? 0/1:"))
    if check:
        print("Прошло", interval, "секунд","\nВаша еда готова можете забрать.")
        break
else:
        print("Ваша еда готова, осторожно горячо.")  