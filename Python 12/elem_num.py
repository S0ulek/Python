def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Не простое")
            break
    else:
        print("Простое")

# ** 0.5 - это по сути взятие корня из числа. Нам нет необходимости проверять числа дальше корня, т.к.
# проверив все множители до корня - мы проверим все возможные варианты делимости числа.

n = int(input("Введите количество чисел в последовательности: "))
for i in range(n):
    new_number = int(input("Введите число: "))
    is_prime(new_number)


# В целом с нашими текущими знаниями этого решения достаточно. Посчитать количество придётся вручную.
# Но решим задачку и вторым вариантом с забеганием вперед:

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


n = int(input("Введите количество чисел в последовательности: "))
count = 0
for i in range(n):
    new_number = int(input("Введите число: "))
    if is_prime(new_number):
        count += 1

print(count)
