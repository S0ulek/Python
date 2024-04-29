def mainMenu():
    print("1. Сделать что то хорошее.")
    print("2. Сделать что то плохое.")
    choice = int(input("Введите номер действия: "))
    if choice == 1:
        good()
    elif choice == 2:
        bad()
    else:
        print("Ошибка ввода. Нужна ввести 1 или 2.")
        mainMenu()


def good():
    print("Всё хорошо.")
    input("Нажмите любую кнопку чтобы вернуться в меню. ")
    mainMenu()

def bad():
    print("Всё плохо.")

mainMenu()