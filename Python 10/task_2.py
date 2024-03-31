size = int(input("Введите размер: "))

for hor in range(1, size + 1):
    for ver in range(hor):
        print(hor, end=" ")
    print()