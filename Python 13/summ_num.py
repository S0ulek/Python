def summa_n(n_in):
    summ_out = 0
    for i in range(1, n_in + 1):
        summ_out += i
    return summ_out


n = int(input("Введите число N: "))
next_n = summa_n(n)
print("Сумма от 1 до", n, "=", next_n)
final_result = summa_n(next_n)
print("Сумма от 1 до", next_n, "=", final_result)