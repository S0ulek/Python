current_width = 8
current_height = 10
width = 15
height = 20
while True:
    print("Марсоход находится на позиции", current_width, current_height)
    command = input("Введите команду:")
    if command == 'W' and current_height < height:
        current_height += 1
    elif command == 'S' and current_height > 1:
        current_height -= 1
    elif command == 'A' and current_width > 1:
        current_width -= 1
    elif command == 'D' and current_width < width:
        current_width += 1
    