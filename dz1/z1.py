while True:
    n = input()
    if n.isdigit():
        print(len(n))
    elif n == 'exit':
        break
    else:
        print("Несоответсвие типов данных")