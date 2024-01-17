money = int(input("Полученные деньги:"))
cheese = 60
ice = 20
if money > cheese:
    print ("На сыр денег хватило")
    if money > (cheese+ice):
        print("На мороженное тоже хватило")
    else:
        print("денег маловато")
if money < cheese:
    print("Денег не хватило даже не сыр")