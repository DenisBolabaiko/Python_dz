n = input("Введите строку: ")
dictionary = {}
for i in n.lower():
    if i != ' ':
        dictionary[i] = dictionary.get(i, 0) + 1 
print(dictionary)
