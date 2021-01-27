"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

dividers = {x: 0 for x in range(2, 10)}

for key in dividers.keys():
    for i in range(2, 100):
        if i % key == 0:
            dividers[key] += 1

for key, value in dividers.items():
    print(f'Для числа {key} в диапазоне от 2 до 99: {value} чисел кратных {key}')



