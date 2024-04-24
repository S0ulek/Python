import math
user_number = float(input("Введите число: "))
print(math.floor(user_number))
print(math.ceil(user_number))
print(abs(user_number))
print(math.sqrt(user_number))
print(math.exp(user_number))
print(math.log(user_number))
print(math.log2(user_number))
print(math.log10(user_number))
print(math.sin(user_number), math.cos(user_number))
if user_number >= 0:
    print(math.factorial(int(user_number)))
else:
    print("Факториал отрицательного числа не определен")
