"""
https://drive.google.com/file/d/1tCS-MVlzHBG5edjjU7cwkiP1vz6rG1pc/view?usp=sharing

task_1
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

a = int(input('Введите трёхзначное число: '))
b = a // 100
c = (a - b*100) // 10
d = a - b*100 - c*10
print(f'Сумма цифр: {b+c+d}')
print(f'Произведение цифр: {b*c*d}')