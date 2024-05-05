start_number = float(input("Введите число: "))
count = 0
while start_number > 0:
    count += 1
    start_number /= 1000

print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")
