debtor = int(input("Введите число должников:"))
debt_sum = 0
for client in range (0, debtor, 5):
    print("Должник с номером", client)
    debt = int(input("Ваша сумма долга:"))
    debt_sum += debt
print("Общая сумма долга:", debt_sum)