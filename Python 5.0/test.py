price = 75000
wallet = int(input("Введите вашу сумму:"))
if wallet >= price:
    wallet -= price
    if wallet < 5000:
     wallet += 1000
    print ("Сделана скидка!")
    print ("Остаток на счету:", wallet)
    print("Курс успешно приобретён!")
else: 
    print("не хватает денег на счету")
print ("Хорошего дня!")




