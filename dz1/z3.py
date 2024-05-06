n = input()
error = False
if n.isdigit() and len(n) == 3:
    for i in range(3):
        for j in range(3):
            if n[i] != n[j]:
                if j != i:
                    for k in range(3):
                        if n[i] != n[k] and n[j] != n[k]:
                            if k != i and k != j:
                                print(n[i] + n[j] + n[k])
                        else:
                            error = True
            else:
                error = True
else:
    print("Ошибка! Введите трехзначное число.")
if error:
    print("Ошибка! Число содержит повторяющиеся цифры.")
