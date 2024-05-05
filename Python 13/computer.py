number = 1
count = 0
save_number = number
while number:
    save_number = number
    number /= 2
    count += 1

print(save_number, count)

