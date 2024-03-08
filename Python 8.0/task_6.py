educational_grant = int(input("Введите степендию:"))
money_spent = int(input("Введите ежемесячный расход:"))
every_months = money_spent
need_money = 0
for month in range (1,11):
    left_money = money_spent - educational_grant
    every_months += every_months/100*3 
    need_money += left_money+(every_months/100*3)

    print (month,every_months, need_money)


    
