first_quarter = int(input("Сумма дохода первого квартала: "))
second_quarter = int(input("Сумма дохода второго квартала: "))
third_quarter = int(input("Сумма дохода третьего квартала: "))
fourth_quarter = int(input("Сумма дохода четвёртого квартала: "))
a,b,c,d = first_quarter,second_quarter,third_quarter,fourth_quarter 
res = (a+b)/(c+d)
print ("Динамика дохода/падения:",res)