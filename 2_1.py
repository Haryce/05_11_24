def rep(m, n, ww=0, crp=[]):
  if m == 0:
    if ww == n:
      print(crp)
    return

  for i in range(1, n - ww + 1):
    crp.append(i)
    rep(m - 1, n, ww + i, crp)
    crp.pop()

#ввод
m = int(input("Введите количество слагаемых (m): "))
n = int(input("Введите число (n): "))
#ввывод
rep(m, n)