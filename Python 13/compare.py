def eqv(a, b, c):
    return abs((a + b) - c) <= 1e-15


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
third = float(input("Введите третье число: "))
print(eqv(first, second, third))
