for attempt in range(1, 4):
 pin = int(input("Введите пин-код: "))
 if pin == 8181:
   print("Пин-код верный")
   break
 print("Неверный пин-код. Осталось попыток:", 3 - attempt)
