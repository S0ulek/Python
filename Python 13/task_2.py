def maximum_of_two(a, b):
    return a if a > b else b

def maximum_of_three(a, b, c):
    return maximum_of_two(a, maximum_of_two(b, c))

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

print ("Максимум из трёх чисел:", maximum_of_three(num1,num2,num3))
