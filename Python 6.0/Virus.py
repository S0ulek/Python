timer = 8
main_tasks = 0
shop = 0
hours = 1
print ("Начался 8 часовой рабочий день." )
while timer != 0:
    print(hours,"час")
    hours += 1
    timer -= 1
    task = int(input("Сколько задач решит Максим?"))    
    main_tasks += task
    call = int(input("Звонит жена. Взять трубку?(1-да/0-нет)"))
    shop += call
print("Рабочий день закончился. Всего выполнено задач:",main_tasks )
if shop != 0:
    print("Нужно зайти в магазин")

