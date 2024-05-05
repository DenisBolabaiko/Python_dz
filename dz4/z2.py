def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = int(input('Введите число: '))
for i in fib(n):
    print(i, end=' ')

