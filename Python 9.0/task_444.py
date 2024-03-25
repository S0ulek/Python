text = input("Введите текст:")
summ = 0 
print("\nОтфильтрованный текст:", end = "")
for symbol in text:
    if symbol == "3" or symbol == "4":
        summ += int(symbol)
    else:
     print(symbol, end = "")
print("\nСумма равна:",summ)