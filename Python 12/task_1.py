import math

num = int(input("Введите число: "))

def summa_n(num):
    result = 0
    for number in range(num + 1):
        result += number       
    print("Я знаю, что сумма чисел от 1 до", num, "равна", result)

summa_n(num)
