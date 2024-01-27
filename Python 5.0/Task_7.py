# time = int(input("Введите время:"))
# if (14<= time <=15) or (10<= time <= 12) or (18<= time <= 20) or (8>time or time>=22):
#     print("Посылку получить нельзя")
# else: 
#     print("Можно получить посылку")

time = int(input("Введите время:"))
if (8<= time <10) or (12<= time <14) or (15<time<18) or (20<=time<22):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")