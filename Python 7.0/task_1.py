positive = 0
for count in range(0, 10):
    users = int(input("Введите число:"))
    if users > 0 and users % 2 == 0:
            positive += 1
print("Количество чётных и положительных чисел:", positive)