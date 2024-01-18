year = int(input("Введите год выпуска:"))
speed_count = int(input("Введите количество скоростей:"))
if year < 2018 or speed_count < 24:
    print("Не подходит")
else:
    print("Подходит")