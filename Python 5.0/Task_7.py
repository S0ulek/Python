time = int(input("Введите время:"))
lunch = (14< time <=15)
packages = (10<= time <= 12) and (18<= time <= 20)
relax_time = (22<= time <8)
if time == lunch or packages or relax_time:
    print("Закрыто")
else: 
    print("Открыто")
