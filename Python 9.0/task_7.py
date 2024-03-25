encrypted_message = input("Введите зашифрованное сообщение: ")
message_1 = ""
message_2 = ""
for index, symbol in enumerate(encrypted_message, start=1):
    if index%2 != 0:
        message_1 += symbol
    elif index%2 == 0:
         message_2 = symbol + message_2
print(message_1 + message_2)    

        
    


