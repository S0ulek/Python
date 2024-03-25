text = input("Введите текст: ")
star = "*"
position = 0

for symbol in text:
    if symbol != star:
     position += 1
    if symbol == star:
       break
print("Символ",star,"стоит на позиции", position)
