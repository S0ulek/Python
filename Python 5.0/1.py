x = int(input("Движение лодки вперед/назад:"))
y = int(input("Движение лодки вверх/вниз:"))

if x<y:
    print("Х меньше Y" )
elif x == y:
    print("X равен Y")
else:
    print("Х больше Y")
