x = int(input("Вклад в банк:"))
p = (x/10)-(x%1)
y = 0
year = 0
while y < 6000:
    y += p
    year += 1
print ("Прошло",year,"лет")