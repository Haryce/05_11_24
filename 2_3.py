def sum(a, b):

    if b == 0:
        return a
    else:
        return sum(a, b - 1) + 1

#ввод
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
#вывод
res = sum(a, b)
print("Сумма чисел:", res)
