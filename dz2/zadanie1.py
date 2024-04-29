n = input("Введите список чисел ").split()
exp = int(input("Введите степень "))
list_ = []
for i in n:
    if i.isdigit():
        i = int(i)
        list_.append(i ** exp)
    else:
        list_.append(i * exp)
print(list)
