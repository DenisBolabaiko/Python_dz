def sum(a, b):
    print(f'Ответ: {a + b}')


def diff(a, b):
    print(f'Ответ: {a - b}')


def umozh(a, b):
    print(f'Ответ: {a * b}')


def razdel(a, b):
    print(f'Ответ: {a / b}')


def exp(a, b):
    print(f'Ответ: {a ** b}')


print("Список операций:")
print("+ Сумма")
print("- Вычитание")
print("* Умножение")
print("/ Деление")
print("^ Возведение в степень")
print("quit Выход из программы")

while True:
    a_1 = float(input("Введите первое число: "))
    b_1 = float(input("Введите второе число: "))
    n = input("Выберите операцию: ")
    if n in ['+', '-', '*', '/', '^', 'quit']:
        if n == '+':
            sum(a_1, b_1)
        elif n == '-':
            diff(a_1, b_1)
        elif n == '*':
            umozh(a_1, b_1)
        elif n == '/':
            if b_1 == 0:
                raise ZeroDivisionError("Деление на ноль!")
            razdel(a_1, b_1)
        elif n == '^':
            exp(a_1, b_1)
        elif n == quit:
            break
        else:
            print("Такой команды нет!")
