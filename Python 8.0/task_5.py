begin = int(input("Введите начало отрезка:"))
end = int(input("Введите конец отрезка:"))
step = int(input("Введите шаг:"))
for y in range (end, begin-1, step ):
    print ("В точке",y,"функция равна:",(y**3+2*y**2-4*y+1))