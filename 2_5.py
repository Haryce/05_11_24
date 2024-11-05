def palindr(s, start, end):
    if start >= end:
        return True
    elif s[start] != s[end]:
        return False
    else:
        return palindr(s, start + 1, end - 1)
#ввод
string = input("Введите строку: ")
start = int(input("Введите начальный индекс (с 1): ")) - 1
end = int(input("Введите конечный индекс: ")) - 1
#ввод
if palindr(string, start, end):
    print(f"Фрагмент строки '{string[start:end + 1]}' является палиндромом.")
else:
    print(f"Фрагмент строки '{string[start:end + 1]}' не является палиндромом.")
