  
def count_letters():
    text = input("Введите текст: ")
    num_to_find = input("Какую цифру ищем?: ")
    let_to_find = input("Какую букву ищем?: ")

    numbers = 0
    letters = 0

    for char in text:
        if char == num_to_find:
            numbers += 1
        elif char.lower() == let_to_find.lower():
            letters += 1

    print("Количество цифр", num_to_find, ":", numbers)
    print("Количество букв", let_to_find, ":", letters)

count_letters()
