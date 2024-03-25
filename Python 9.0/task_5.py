text = input("Введите текст: ")
word = ""
longest_length = 0

for char in text + " ":  
    if char != " ":
        word += char
    else:
        word_length = 0
        for symbol in word:
            word_length += 1
        if word_length > longest_length:
            longest_length = word_length
        word = ""
print("Самое длинное слово",longest_length, "букв")
