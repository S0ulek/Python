# В свободное время Вася любит играть в компьютерные игры. Однажды у него появилась классная идея для сюжета игры.
 #Чтобы воплотить её в жизнь, он начал изучать геймдизайн. Создавать игру он начал с главного героя и его системы прокачки.

# Напишите программу, которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень. 
#Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.

# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4

# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2


#lvl = "Ваш уровень: 1"

#xp = int(input("Введите очки опыта :"))

#if xp >=1000 and xp <=2499: 
 #   lvl = "Ваш уровень:2"
  #  print(lvl)
#elif xp >=2500 and  xp <=4999:
 #   lvl = "Ваш уровень: 3"
  #  print(lvl)
#elif xp ==5000 or xp >5000:
 #   lvl = "Ваш уровень: 4"
  #  print(lvl)
#else:
 #   print(lvl)    


# Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:


# Напомним, как это работает:
# Если X больше нуля Y = X - 12.
# Если X равных нулю Y равен пяти.
# Если X меньше нуля Y равен квадрату X.

# Пример:
# Введите икс: 0
# Игрек равен 5

# Пример 2:
# Введите икс: -6
# Игрек равен 36


#x = int(input("Введите число :"))

#if x>0:
 #   y = x -12
  #  print(y)

#elif x ==0:
 #   y = 5
  #  print(y)

#elif x<0:
 #   y = x**2
  #  print(y)


#place = int(input("Введите место в списке :"))
#point = int(input("Введите количество баллов : "))



#if point >=290 and place <=10:
 #   print("Поздравляю вы поступили!""\nБонусом вам будет начисляться стипендия")

#elif point <290 and place <=10:
 #   print("Поздравляю вы поступили""\nНо вам не будет начисляться стипендия")
#else:
 #   print("К сожалению вы не поступили")

# rating = int(input('Что получил по математике? '))

# if rating  ==2 or rating ==3:
#     print('Плохо. Марш учиться!')

# elif rating  ==4 or rating==5:
#     print('Молодец! Можешь отдохнуть.')

# first = int(input("Введите первое число :"))
# second = int(input("Введите второе число :"))
# third = int(input("Введите третье число :"))

# if first == third == second :
#     print(3)
# elif first == second or second == third or third == first :
#     print (2)
# else:
#     print(0)

# price = int(input("Введите стоимость квартиры:"))
# place = int(input("Введите кв :"))

# if place >=100 and price <10000000:
#     print(" Подходит")

# elif  place >=80 and place <100 and price <7000000:
#     print("Подходит")

# else:
#     print(" Не подходит ")    


# time = int(input("Введите желаемое время получения :"))

# if ( 14<= time <=15) or (10<= time <=12) or  (18<= time <=20)  or time <8 or time >=22: 
#     print (" polucit nelza")

# else:
#     print ("mojete polucit posilku")    


# number =int(input('Введите число: '))
# while number > 0:
#     number = int(input('Введите число: '))
#     total = int(input('Введите число: '))
#     print ( number + total) 

# print(number)


# number = int(input('Введите число: '))
# while number > 0:
#      number = int(input('Введите число: '))
#      total = number + number 
#      print ( total) 

# print(number)

   

# def func(a,b):
#     res = a + b
#     #print("Result",res)
#     return res


# res = func(5,7)    
# print (res)
# print("i","l")

# def minimal(l):
#     mini = l[0]
#     for el in l:
#         if el < mini:
#             mini=el
     
#     print(mini)


    

# nums1 = [5, 7, 2, 9, 4]
# minimal(nums1)

# min = nums1[0]
# for el in nums1:
#      if el < min:
#          min=el

# print(min)        



# nums1 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]

# min = nums1[0]
# for el in nums1:
#      if el < min:
#          min=el

# print(min)       

# func = lambda x,y: x * y

# res = func(8,9)

# print(res)

# number = int(input("Введите число для проверки:"))
# num = 0

# while number >= 0:
#     number = int(input("Введите число для проверки:"))
#     num += 1
#     if number <0:
#         print(num,"\nОбнаружен минус")

    
    

# kod = int(input("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки \nВведите код :"))

# password = 222

# while True:
#      kod = int(input("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки \nВведите код :"))
#      if kod ==222:
#          print("Код верный." "\nЗавершаю работу...")
#          break



# money = int(input("Введите бабосики : "))

# qepiki = money 

# while  qepiki <10000:
#     kubik = int(input("че выпало? : "))
  
#     if kubik != 3:
#         qepiki +=500
#         print("Вы выйграли 500 гяпиков!" )

#     elif kubik ==3:
#         qepiki -= qepiki
#         print ("Вы банкрот!")
#         break

# print ("Игра окончена.", "\nИтого гяпиков: ",qepiki)



# count = 10
# while True:
#     if count == 0:
#         print('Время вышло!')
#         break
#     else:
#         print(count)
#         count -= 1

# while True:
#     rabota = int(input("Продолжаем работать? 1/0:"))
#     if rabota ==0:
#         print("Приложение закрываеться...", "\nРабота завершена.")
#         break




# count = int(input("Сколько раз поовторить? :"))

# proger = 0

# while proger < count:
#     print("я -Программист!")
#     proger +=1


# bags = int(input("skolka meskov?: "))

# totalweight= 0
# bagscount = 0

# while  bagscount < bags:
#     weight = int(input("ves meska?: "))
#     totalweight +=weight
#     bagscount +=1

# print("Obsi ves :", totalweight)


# num = int(input("Введите число : "))

# nums = 0

# while nums < num :
#     nums +=1 
#     print( nums, "**" , num,"=", nums ** num)
    
    
# name = input("Введите свое имя : ")

# borc = int(input("Введите сумму  задолжнности : "))

# print(name," Ваша задолженность :", borc,"рублей")

# money = 0

# while money < borc:
#     qepik = int(input("Сколько рублей внесете прямо сейчас, чтобы её погасить? : "))
#     money +=qepik
#     print("Маловато" , name ,  "давайте еще!")

# print ("Отлично" ,name +"!",  " Вы погасили долг спасибо!")   



# plus = 0
# minus = 0

# while True:
#     num= int(input("Введите оценку! : "))
#     if num > 0 :
#         plus += 1
#     elif num <0:
#         minus +=1
#     else:
#         print("Кол-во положительных оценок :" , plus, "\nКол-во отрицательных оценок :", minus)
#         break
        

     
# print ("Начался 8-часовой рабочий день")

# hour = 0
# task = 0
# wife = False

# while hour<=7:
#   hour+=1
#   print(hour, "час")
#   time = int(input("Сколько задач решит Максим? : "))
#   task +=time
#   wifi = int(input("Звонит жена. Взять трубку? (1-да, 0-нет) : "))
#   if wifi >0:
#     wife = True

# print("Рабочий день закончен. выполнено задач :",task)

# if wife:
#   print("Нужно в магазин зайти")

# vklad = int(input("Укажите ваш вклад? :"))
# y = 6000
# scet = 0
# years = 0

# while scet < y:
#     scet +=vklad
#     years +=1
#     scet += vklad%10
#     scet //10

# print(years,scet)




# win = 7
# trying = 0

# while True:
#     trying +=1
#     num = int(input("Введите число :"))
#     if num < 7:
#         print("Число меньше чем нужно. Попробуйте еще раз!")
#     elif num >7:
#         print ( "Число больше чем нужно. Попробуте еще раз!")
#     else:
#         print("Вы угадали! число попыток:", trying)
#         break






 






# num =101
# num2 =0

# tryng = 0

# while tryng <7:
#     nums= (num+num2)//(2)
#     tryng +=1
#     print("Твое число равно, меньше или больше, чем число",nums,"?")
#     ask=int(input())
#     if ask ==1:
#         print("Я гений!")
#         break
#     elif ask ==2:
#         num =nums

#     elif ask ==3:
#         num2=nums
    



# dolg = int(input("Введите числа :"))
# doljniki = 0

# for pepa in range(dolg):
#     if dolg /2 and dolg > 0:
#         doljniki +=1


# print (" кол-во говнюков :",doljniki )        


# doljniki = 0


# for dolg in range(10):
#     ask = int(input("Введите число :"))
#     if ask % 2 == 0 and ask >0:
#         doljniki +=1
    
# print("Кол-во Должников -",doljniki)


# month = 0
# money = 0

# for boss in range (0,12):
#     month +=1
#     print("месяц",month)
#     zp = int(input("Введите зарплату за этот месяц : "))
#     money +=zp


# print("Средняя зарплата за год :", money //12)




fakt = int(input("Vvedite cislo : "))
umnoj = 1
umnoj2 = 1


for jopa in range(1,fakt ):
    umnoj2+=1
    umnoj *= umnoj2
    
    
    
  
    
print(umnoj)    
    


      
    


    


  


  




  


  



    
    
    

   

    
    
        
    
    


