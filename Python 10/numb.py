seqNum = int(input("Сколько будет чисел: "))
numeral = int(input("Какую цифру считать: "))
while numeral < 0 or numeral > 9:
    numeral = int(input("Цифры должна быть в диапазоне от 0 до 9. \nВведите новую цифру: "))
numeralCount = 0
for num in range (seqNum):
    print("Введите", num, "число:", end = "")
    number = int(input())
    while number > 0:
        if number % 10 == numeral:
            numeralCount += 1
        number //= 10
print("Цифр", numeral, "в последовательности", numeralCount)
