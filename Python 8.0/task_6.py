educational_grant = int(input("Введите степендию:"))
money_spent = int(input("Введите ежемесячный расход:"))
need_money = 0
for month in range (1,11):
    need_money += money_spent - educational_grant
    print(month,"месяц траты",round(money_spent, 2),"не хватает",round(need_money, 2))
    money_spent *= 1.03   
print("Нужно попросить",round(need_money, 2),"рублей")
    
