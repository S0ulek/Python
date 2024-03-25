string = input("Введите строку:") #aabc
prevsym = ""
equalsym = False
for letter in string:
    if prevsym == letter:
        equalsym = True
        break
    else:
        prevsym = letter

if equalsym:
    print("Есть две одинаковвые буквы подряд")
else:
    print("Совпадений нет")
