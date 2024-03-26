message = input("Введите текст:")
polindrom = ""
for symbol in message:
   if symbol != " ":
      polindrom = symbol + polindrom
   
if polindrom == message.replace(" ", ""):
   print("Да, это палиндром")
else:
   print("Нет,это не палиндром")