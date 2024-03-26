message = input("Введите текст:")
polindrome = ""
for symbol in message:
   if symbol != " ":
      polindrome = symbol + polindrome
   
if polindrome.lower() == message.lower():
   print("Да, это палиндром")
else:
   print("Нет, это не палиндром")
