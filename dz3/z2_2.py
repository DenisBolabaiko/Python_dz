elements = lambda in_list, mnozh=2: [x * mnozh for x in in_list]

in_list = []
n = map(int, input("Введите список: ").split())
for i in n:
    in_list.append(i)
choise = str(input("Хотите ли выбрать множитель? Y/n "))
if choise.lower() == 'n':
    rez = elements(in_list)
    print(rez)
elif choise.lower() == 'y':
    mnozh = int(input("Введите множитель: "))
    rez = elements(in_list, mnozh)
    print(rez)
