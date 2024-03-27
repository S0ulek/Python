team = 0
for answer in range (10):
    answer = input("Крикните команду!:")
    if answer.capitalize() == "Карамба":
        team += 1
        print("Добро пожаловать на борт!")
print("Новых членов экипажа:", team)
