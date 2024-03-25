a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
count = 0
sum = 0
for res in range(a,b+1) :
  if res%c == 0:    
   sum += res
   count += 1    
if count >0:
 print ("Среднее арифметическое чисел из отрезка, кратных числу",c,"равно",int(sum/count))
else: 
 print("В отрезке нет чисел, кратных числу", c)