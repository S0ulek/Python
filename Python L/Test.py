#print("results:", 7,6,8, sep="|", end=("\n"))

#print(round(5/7))

#input("enter password:")

#digit = 4.56665
#word = "loli"

#print(word,digit)


#number = 5

#print("results:",number)

#del number
#number = 7

#print("results:",number)


first_cube = int(input("Введите очки : "))
second_cube = int(input("Введите очки : "))

if first_cube >= second_cube:
    print(first_cube - second_cube, "\nИгрок платит")

else:
    print(first_cube + second_cube, "\nВладелец платит")

print("Игра окончена.")