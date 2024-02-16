number = 7
user = int(input("Угадайте число:"))
count = 0
while user < number:
    print("Число меньше, чем нужно. Попробуйте ещё раз!")
    user = int(input("Угадайте число:"))
    count += 1
    if user > number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
        user = int(input("Угадайте число:"))
        count += 1
else:
    count += 1
    print("Вы угадали число. Число попыток:",count)