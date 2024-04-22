bet = int(input("Сделайте вашу ставку:"))
coef = float(input("Введите коэфицент:"))

win = round(bet * coef,2)
print ("Выйгрыш составляет:", win)