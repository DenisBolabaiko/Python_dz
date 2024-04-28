end = int(input())
start = -end
count_plus = 0
count_minus = 0
while start != end + 1:
    print(start, end=' ')
    if start < 0:
        count_minus += start
    elif start > 0:
        count_plus += start
    start += 1

print(f"\nСумма отрицательных чисел = {count_minus}")
print(f"Сумма положительных чисел = {count_plus}")

