#алгоритм вычисления НОД двух чисел
def nod(a, b):
  if b == 0:
    return a
  else:
    return nod(b, a % b)
#алгоритм вычисления значения очередного числа Фибоначчи   
def fibon(n):
  if n <= 1:
    return n
  else:
    return fibon(n-1) + fibon(n-2)
#рекурсивная функция переворачивающая заданное натуральное число
def rev(n):
  if n < 10:
    return n
  else:
    return int(str(n % 10) + str(rev(n // 10)))
# Ввод данных
q = int(input("Введите первое число для вычисления НОД: "))
w = int(input("Введите второе число для вычисления НОД: "))
n = int(input("Введите номер числа Фибоначчи: "))
num = int(input("Введите натуральное число для переворота: "))
# Вывод результатов
print(f"НОД ({q}, {w}) = {nod(q, w)}")
print(f"{n} число Фибоначчи = {fibon(n)}")
print(f"Перевернутое число {num} = {rev(num)}")