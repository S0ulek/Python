import math

count = int(input("Введите кол-во чисел: "))
for _ in range (count):
 numb = float(input("Введите число: "))
 logx = 0
 if numb > 0:  
  logx += math.ceil(numb)
  print (math.log(logx))
 elif numb < 0:
  logx += math.floor(numb)
  print (math.exp(logx))