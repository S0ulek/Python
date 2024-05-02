def Calc():
    print("1. Вывести сумму цифр.")
    print("2. Вывод максимальной цифры.")
    print("3. Вывод минимальной цифры")
    action = int(input("Что вы хотите сделать? "))
    if action == 1:
        number = int(input("Введите число: "))
        summ(number)
    elif action == 2:
        number = int(input("Введите число: "))
        max_n(number)
    elif action == 3:
        number = int(input("Введите число: "))
        min_n(number)
    else:
        print("Такой функции не существует.")
        Calc()
    

def summ(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    print("Сумма цифр числа:", total)
    print()
    Calc()

def max_n(number):
    max_n = 0
    while number > 0:
        digit = number % 10
        if digit > max_n:
            max_n = digit
        number //= 10
    print("Максимальная цифра числа:", max_n)
    print()
    Calc()

def min_n(number):
    min_n = 9
    while number > 0:
        digit = number % 10
        if digit < min_n:
            min_n = digit
        number //= 10
    print("Минимальная цифра числа:", min_n)
    print()
    Calc()

Calc()