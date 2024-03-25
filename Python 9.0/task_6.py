earned_milk = 0
place = input("Введите стойла:")
for index, symbol in enumerate(place, start=1):
   if symbol == "b":
      earned_milk += 2*index
print("Собрано молока:", earned_milk)
      
