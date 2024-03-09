boys = int(input("Введите число мальчиков:"))
girls = int(input("Введите число девочек:"))
people = boys + girls
sitting = ""

if people%2>0:
   print("нет решения")
if people%2 == 0:
 for place in range (0,people, 2):
  boys -= 1
  girls -= 1
  if boys != 0:
   sitting += "B"
   if girls != 0:
    sitting += "G"
 print(sitting) 

  

   




