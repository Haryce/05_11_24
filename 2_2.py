def dfact(u):
  if u == 0 or u == 1:
    return 1
  else:
    return u * dfact(u - 2)
#ввод
u = int(input("Введите число для вычисления двойного факториала: "))
#вывод
res = dfact(u)
print(f"{u}!! = {res}")