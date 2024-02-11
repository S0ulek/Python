name = input("Введите своё имя: ")
credit = int(input("Введите сумму долга: "))
print (name,"ваша задолжность составляет",credit,"рублей")
money = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?"))
while money < credit:        
    print ("Маловато",name,"!","Давайте ещё раз.")
    print (money)
else:
  print ("Отлично",name + "!","Вы погасили долг. Спасибо!")

    
                   