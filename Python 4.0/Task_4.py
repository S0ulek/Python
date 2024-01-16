first_price = int(input("Цена первого товара: "))
second_price = int(input("Цена первого товара: "))
third_price = int(input("Цена третьего товара: "))
sum = (first_price+second_price+third_price)
limit_price = 10000
if sum > limit_price:
    print (sum-(sum*10)//100)
else: 
    print (sum)
   