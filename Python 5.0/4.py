first = int(input("Вес первой монеты:"))
second = int(input("Вес второй монеты:"))
third = int(input("Вес третьей монеты:"))
if first == second:
    print("Третья монета легче")
elif second == third:
    print("Первая монета легче")
else:
    print("Вторая монета легче")