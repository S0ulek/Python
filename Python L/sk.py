#client = 'Петя'
#print(client)
#print(' и ')
#pet = "кот"
#print(pet)


#r = 'Red'
#g = 'Green'
#b =  'Blue'
#print(b, g, r+g+b, b, g + b,)





#firstanimal ="bunny"
#secondanimal ="turtle"

#print(firstanimal, "sleep",",", secondanimal ,"walking"  ".")



#firstname = input("enter user name:")
#hello = "доброе утро,"
#print(firstname,hello)
#intro = "к сожалению, у вас нет доступа к системе."
#info = "Пожалуйста, обратитесь к системному администратору."
#print(intro,"\n",info)





#fly = input("введите город вылета:")
#arrival = input("введите город прилета:")
#print (fly,"-" ,arrival)

#pep = "pepka osujdaet"

#if fly == "baku":
 #   print("примерное время полета 6 часов")
    
#elif fly == "moskva":
 #   print("примерное время полета 20 часов" )
#else:
 #   print(pep)



#for data in range(2,9,3):
 #   print(data)


#count = 0

#word = "hello pepa"

#for i in word:
 #   if i == "l":
  #      count += 1

    
#print ("count" , count)

#Ishascat = True

#while Ishascat:
 #   if input("Enter data: ") == "Stop":
  #      Ishascat = False


#for i in range(11):
 #   if i == 5:
  #      break

   # if i % 2 == 0:
    #    continue
    
   # print(i)


#Found = None

#for i in "hello":
 #   if i == "l":
  #      found = True
   #     break
#else:
 #   found = False

#print(found)          



#nums = [5,7,2,4,7, True, "hello", 6.7,[5,7]]

#nums[0]=50

#nums[5] = 1.01
#print (nums[-1][1])


#numbers = [5,2,7]
#e = [5,6,8]
#numbers.append(100)
#numbers.insert(1,True)
#numbers.extend(e)
#numbers.sort()
#numbers.reverse()

#numbers.pop(2)
#numbers.remove(True)

#numbers.clear()




#print(len(numbers))

#print(numbers.count(5))

#nums = [5,2,7,"50", False]

#for el in nums:
 #   el*= 2
  #  print(el)

#n = int(input("Enter lenght: "))

#user_list = []

#i = 0

#while i < n:
 #   string = "Enter element #" + str(i + 1) + ": "
  #  user_list.append(input(string))
   # i += 1

#print(user_list)    

#word = "itproger, hool, pepka"
#print (word.count(""))


#print(word.islower())

#print(word.lower())

#print(word.isupper())

#print(word.capitalize())
#hobby = word.split(", ")

#for i in range(len(hobby)):
 #   hobby[i] = hobby[i].capitalize()

#result = ", ".join(hobby)    

#print(result)    





#country = {"code": "RU", "name": "Russian","population": 144}

#country = dict(code="RU", name="russian")

#for key, value in country.items():
   # print(key, "-" , value)

#print(country.get("code"))

#country.popitem()

#country["code"] = "none"
#print(country.items())


person = {
    "user_1":{
       "first_name":"jonh",
       "last_name": "marley",
       "age": 45,
       "address": ["c.moskow","street tot","45"],
       "grades": {"math": 5, "physics": 3}}}





print(person["user_1"]["address"][1])
