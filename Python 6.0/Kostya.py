money = int(input("Введите начальную сумму: "))

while money < 10000:
    kubik = int(input("Введите число на кубике(1-6):"))
    if kubik == 3:
        money = 0
        print("Вы проиграли всё","\nИгра окочена","\nОсталось", money,"рублей")
        break
    money += 500
    print("Выйграли 500 рублей!","\nИгра закончена","\nИтого осталось:", money,"рублей")