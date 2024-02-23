max =101
min =0
trying = 0
while trying <7:
    N= (max+min)//(2)
    trying +=1
    print("Твое число равно, меньше или больше, чем число",N,"?")
    ask=int(input())
    if ask ==1:
        print("Я гений!")
        break
    elif ask ==2:
        min = N
    elif ask ==3:
        max = N
    
