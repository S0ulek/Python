n = int(input("Введите число:"))
elem_summ = 0
for number in range(n):
    print("При N =", n, "элементы выражения будут равны:")
    print("n =",number)
    elem = ((-1)**number * 1/(2**number))
    elem_summ += elem
    print("elem =",elem)  
print("Сумма равна:",elem_summ)
    

    
