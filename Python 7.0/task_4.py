students = int(input("Введите число учеников:"))
normal = 0
good = 0
excellent = 0
stud_num = 0
for rating in range(students):
    stud_num += 1
    print ("Какую оценку получил ученик номер", stud_num)
    r = int(input())
    if r == 3:
        normal += 1
    elif r == 4:
        good += 1
    elif r == 5:
        excellent += 1
if normal < excellent > good:
    print ("Сегодня больше отличников")
elif excellent < good > normal:
    print ("Сегодня больше хорошистов")
elif excellent < normal > good:
    print("Сегодня больше троечников")