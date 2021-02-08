"""
Урок 2, задание 3. Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран. Например, если
введено число 3486, надо вывести 6843.
"""

import sys

num = input('Введите натуральное число: ')
res = ''
for i in num[::-1]:
    res += i
print(f'Обратное по порядку цифр число: {res}')


def calculate_size(obj):
    get_size_of = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items:
                get_size_of += calculate_size(key)
                get_size_of += calculate_size(value)
        elif not isinstance(obj, str):
            for item in obj:
                get_size_of += calculate_size(item)
    return get_size_of


print(calculate_size(num))

# Для 64 битной версии Python:
# Количество занятой памяти для числа "98" равно 51 байт
# Количество занятой памяти для числа "459" равно 52 байта
# Количество занятой памяти для числа "123456789" равно 58 байт
# Количество занятой памяти для числа "123456789876543212345678765432123456787654321" равно 94 байта
# По количеству занятой памяти данный способ решения является самым оптимальным
