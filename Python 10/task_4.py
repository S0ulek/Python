count = int(input("Введите кол-во чисел:"))
num_count = 0

for _ in range (count):
    number = int(input("Введите число:"))
    isPrime = number > 1
    for divider in range (2, number):
        if number % divider == 0:
            isPrime = False

    if isPrime:
        num_count += 1
print("Количество простых чисел в последовательности:", num_count)
