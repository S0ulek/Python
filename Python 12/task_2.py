def test():   
    number = int(input("Введите число: "))
    if number >= 0:
        positive()
    elif number < 0:
        negative()    

def positive():
    print("Положительное")
    test()

def negative():
    print("Отрицательное")
    test()

test()