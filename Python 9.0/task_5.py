text = input("Введите текст: ")
head = ""
longest_length = 0

for char in text:
   if is_head:
       head += char
       is_head = False
   else:
       tail = char + tail
       is_head = True
print("Самое длинное слово",longest_length, "букв")
