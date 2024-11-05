def umn(a, b):
    if b == 0:
        return 0
    else:
        return a + umn(a, b - 1)
#ввод
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
#вывод
result = umn(a, b)
print(f"{a} * {b} = {result}")
