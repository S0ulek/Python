timer = 0
main_tasks = 0
shop = False
hours = 0
print ("Начался 8 часовой рабочий день." )
while timer < 8:
    hours += 1
    print(hours,"час")    
    timer += 1
    task = int(input("Сколько задач решит Максим?"))    
    main_tasks += task
    call = int(input("Звонит жена. Взять трубку?(1-да/0-нет)"))
    if call == 1:
        shop = True
print("Рабочий день закончился. Всего выполнено задач:",main_tasks )
if shop:
    print("Нужно зайти в магазин")
    

