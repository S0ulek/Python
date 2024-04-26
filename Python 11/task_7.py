fisrt_num = int(input("Введите первое число: "))
sec_num = int(input("Введите второе число: "))

res = ((fisrt_num + sec_num) + abs(fisrt_num - sec_num)) // 2

print("Наибольшее число:", res)
