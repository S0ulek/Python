number = int(input("Введите число:"))
for row in range(number+1):
    for col in range(number+1):
        print(col*2+row,end="\t")
    print()