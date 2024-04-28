name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")
ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
while True:
    shoot = input("Введите коорднаты для выстрела: ")
    shoot = shoot.upper()
    
    if shoot[0].isdigit:
        print("Сначала должна быть буквенная координата!")
    else:
        if shoot in ship:
            print("Попадание!")
        else:
            print("Мимо.")
