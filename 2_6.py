def qw(num):
    if num == 0:
        return 0
    else:
        return 1 + qw(num // 10)
#ввод
n = int(input("Введите число: "))
#вывод
result = qw(n)
print(f"Количество цифр в числе {n}: {result}")
