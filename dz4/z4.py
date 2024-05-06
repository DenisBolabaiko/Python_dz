def decorator(fun):
    def wrap(*args, **kwargs):
        print(f"Функция: {fun.__name__}")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        return fun(*args, **kwargs)
    return wrap


@decorator
def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = int(input('Введите число: '))
for i in fib(n):
    print(i, end=' ')