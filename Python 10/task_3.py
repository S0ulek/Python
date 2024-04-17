width = int(input("Введите ширину:"))
height = int(input("Введите длину:"))

for y in range(height):
    for x in range(width):
        if y == 0 or y == height -1:
            print('-', end='')
        elif x == 0 or x == width - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()
