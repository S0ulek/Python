count = int(input("Введите число карточек:"))
counter = 0
sum = 0
for card_num in range (1, count+1):
    counter += 1
    sum += card_num
    if counter != 1:
        known_card = int(input("Введите номер карты:"))
        counter -= 1
        sum -= known_card
print("Номер пропавшей карты:",sum)

   
