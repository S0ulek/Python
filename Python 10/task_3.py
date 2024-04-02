width = int(input("Введите ширину: " ))
height = int(input("Введите высоту: "))

for up in range (height):
    for side in range (width):
      if up == 0 or up == height:
        print("-", end="")
      elif side == 0 or side == width:
        print("|", end="")
    else:
       print()