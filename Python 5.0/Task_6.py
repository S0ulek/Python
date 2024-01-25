area = int(input("Количество квадратных метров: "))
price = int(input("Цена квартиры: "))

if (area >= 100 and price <= 10) or (area >=80 and price <= 7):
    print("Квартира подходит!")
else: 
    print("Квартира не подходит")