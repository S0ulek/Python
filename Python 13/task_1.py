def convert_to_float_format(x):
    b = 0
    while x >= 10:
        x /= 10
        b += 1
    while x < 1:
        x *= 10
        b -= 1
    return x, b

x = float(input("Введите положительное число: "))
if x <= 0:
    print("Число должно быть положительным.")
else:
    a, b = convert_to_float_format(x)
    print(f"Формат плавающей точки: x = {a} * 10 ** {b}")
