count = int(input("Введите число карточек:"))
x = 0
sum = 0
for card in range (1, count+1):
    x += 1
    sum += card
    while x != 1:
        cart = int(input("Введите номер карты:"))
        x -= 1
        sum -= cart
print("Номер пропавшей карты:",sum)

   
