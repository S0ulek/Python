num = int(input("Введите первое число:"))
step = int(input("Введите шаг:"))
sum = 0

print("\nIP-adress:", end = "")
for count in range(3):
    print(num, end = ".")
    sum += num
    num += step
print(sum)