number = int(input("Введите число:"))
for row in range(number+1):
    for col in range(number+1):
        print(col+row,end="\t")
    print()