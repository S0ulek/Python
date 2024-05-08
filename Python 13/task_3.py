def reverse_number(num):
    return int(str(num)[::-1])

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

reversed_sum = reverse_number(num1) + reverse_number(num2)

reversed_result = reverse_number(reversed_sum)

print("\nПервое число наоборот:", reverse_number(num1))
print("Второе число наоборот:", reverse_number(num2))
print("\nСумма:", reversed_sum)
print("Сумма наоборот:", reversed_result)


