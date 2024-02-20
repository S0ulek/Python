middle_salary = 0
test = 0
for months in range (0, 12):
    test += 1
    salary = int(input("Введите зарплату за",test, "этот месяц:" ))
    middle_salary += salary
print ("Средняя зарплата составляет", middle_salary//12)
    
    