first_num = int(input("Введите первое число:"))
sec_num = int(input("Введите второе число:"))
count = 0
sum = 0
for res in range(first_num, sec_num +1) :
  if res%3 == 0:    
   sum += res
   count += 1    
print ("Среднее арифметическое введённых числе равно:", sum/count)

