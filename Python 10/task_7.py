height = int(input("Введите высоту пирамиды: "))
pyr = 1
for num in range(height):
    for empty in range(height - num - 1):
        print(" ", end="")
    for fill in range(num + 1):
        print(pyr, end=" ")
        pyr += 2        
    print()
