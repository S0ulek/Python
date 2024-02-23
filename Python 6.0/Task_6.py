deposit = int(input("Вклад в банк:"))
percent = int(input("Введите процент:"))
total = int(input("Нужная сумма:"))

year = 0
while deposit < total:    
    deposit += (deposit*(percent*0.01))
    year += 1      
    deposit = int(deposit) 
print ("Прошло",year,"лет")
print(deposit)