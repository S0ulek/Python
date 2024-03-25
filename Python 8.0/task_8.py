boys = int(input("Введите кол-во мальчиков: "))
girls = int(input("Введите кол-во девочек: "))
seating = ""
if boys > 2 * girls or girls > 2 * boys:
    print("Нет решения")
elif boys >= girls:
   people = boys - girls
   for bgb in range (people):
       seating += "BGB"
   for bg in range(girls - people):
       seating += "BG"
else:
    people = girls - boys
    for gbg in range (people):
       seating += "GBG"
    for gb in range (boys - people):
       seating += "Gb"
print(seating)


   




