first_num = int(input("Введите первое число:"))
sec_num = int(input("Введите второе число:"))
num = first_num
count = 0
sum = 0
for res in range(first_num, sec_num):
  num += 1
  if num%3 == 0:    
   sum += num     
   count += 1    
print ("Среднее арифметическое введённых числе равно:", sum/count)