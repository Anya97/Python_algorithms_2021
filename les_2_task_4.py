"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Введите число членов рядов: '))
def series_sum(n, res, i):
    if n != 0:
        res += i
        i = -0.5*i
        return series_sum(n - 1, res, i)
    else:
        return res
result = series_sum(n, res = 0, i = 1)
print(f'Сумма {n} членов ряда равна: {result}')