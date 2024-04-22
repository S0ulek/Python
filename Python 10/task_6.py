height = int(input("Введите высоту пирамиды: "))

for num in range(height):
    for empty in range(height - num - 1):
        print(" ", end="")
    for sym in range(2 * num + 1):
        print("#", end="")
    print()
