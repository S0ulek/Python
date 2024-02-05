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



num = int(input("Vvedite cislo : "))


while num !=0:
    nums =len(num)
    print(nums)

   

    
    
        
    
    


