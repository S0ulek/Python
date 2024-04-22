height = float(input("Ваш рост: "))
weight = float(input("Ваш вес: "))

bmi = weight / height ** 2
print ("Индекс массы вашего тела:", round(bmi, 2))

if bmi < 18.5:
    print("У вас недостаточная масса тела")
elif bmi < 25:
    print("У вас нормальная масса тела")
elif bmi < 30:
    print("У вас избыточный вес")
else:
    print("У вас ожирение")