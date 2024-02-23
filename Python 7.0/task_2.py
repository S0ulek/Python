middle_salary = 0
for months in range (0, 12):
    salary = int(input("Введите зарплату за этот месяц:" ))
    middle_salary += salary
print ("Средняя зарплата составляет", middle_salary//12)
    
    