start_number = float(input("Введите число: "))
count = 0
while start_number > 10:
    count += 1
    start_number /= 10

print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")
