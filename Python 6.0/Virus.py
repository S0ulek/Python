password = 550
password = False
while True:
    user = int(input("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!\nВведите Код:"))
    if user == password:
        print("Можешь работать")
        break