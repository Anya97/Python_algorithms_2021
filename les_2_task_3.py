"""
3. Сформировать из введенного числа обратное по порядку 
входящих в него цифр и вывести на экран. Например, если 
введено число 3486, надо вывести 6843.
"""

num = int(input('Введите натуральное число: '))
def recursion(num, i):
    if num > 0:
        r = num % 10
        num = num // 10
        i = i*10 + r
        return recursion(num, i)
    else:
        return i
res = recursion(num, i=0)
print(f'Обратное по порядку цифр число: {res}')