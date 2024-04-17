n = int(input("Введите количество чисел: "))
max_number = 0
max_sum = 0

for _ in range(n):
    number = int(input("Введите число: "))
    current_sum = 0
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        current_sum += digit
        temp_number //= 10
    if current_sum > max_sum:
        max_sum = current_sum
        max_number = number

print("Число с наибольшей суммой цифр:", max_number, "\nСумма чисел равна:", max_sum)
