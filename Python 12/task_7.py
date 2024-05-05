def rock_paper_scissors():
    print("Игра 'Камень, ножницы, бумага'")
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    computer_choice = "камень"

    if user_choice == computer_choice:
        print("Ничья!")
    elif user_choice == "камень" and computer_choice == "ножницы" or \
            user_choice == "ножницы" and computer_choice == "бумага" or \
            user_choice == "бумага" and computer_choice == "камень":
        print("Победа! Пользователь победил компьютер.")
    else:
        print("Поражение! Компьютер победил пользователя.")

def guess_the_number():
    print("Игра 'Угадай число'")
    secret_number = 42 

    while True:
        guess = int(input("Угадайте число (от 1 до 100): "))
        if guess == secret_number:
            print("Поздравляем! Вы угадали число!")
            break
        else:
            print("Неправильно. Попробуйте ещё раз.")

def main_menu():
    print("Главное меню игры")
    print("1. Играть в 'Камень, ножницы, бумага'")
    print("2. Играть в 'Угадай число'")
    choice = input("Выберите игру (1 или 2): ")

    if choice == "1":
        rock_paper_scissors()
    elif choice == "2":
        guess_the_number()
    else:
        print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")

main_menu()
