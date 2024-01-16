first_num = int(input("Кубик игрока: "))
second_num = int(input("Кубик владельца: "))

if first_num >= second_num:
    print ("Итог:", first_num-second_num)
    print ("Игрок платит")
else:
    print("Итог:", first_num+second_num)
    print("Владелец платит")
print("Игра окончена")
