
start = float(input("Введите начальную амплитуду: "))
end = float(input("Введите амплитуду остановки: "))
   

swings = 0
while start > end:
    start *= 0.916
    swings += 1

print("Маятник считается остановившимся через", swings,"колебаний")
