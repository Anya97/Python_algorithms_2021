"""
task_5
5. Пользователь вводит две буквы. Определить, на каких местах 
алфавита они стоят, и сколько между ними находится букв.
"""
a = str(input('Введите первую букву: '))
b = str(input('Введите вторую букву: '))
c = ord(a) - 96
d = ord(b) - 96
if c != d:
    print(f'{a}: {c}, {b}: {d}, количество букв между {a} и {b}: {abs(d - c) - 1}')
else:
    print(f'{a}: {c}, {b}: {d}, буквы совпадают')