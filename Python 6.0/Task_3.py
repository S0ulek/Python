number = int(input("Введите число:"))
answer = 0
while number != 0:
    last_num = number%10
    answer +=1
    number //10
print(answer)
