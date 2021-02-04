"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3,
           '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3',
           4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
           9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

new_list = []
num_1 = input('Введите первое шестнадцатиричное число: ')
num_list_1 = list(reversed(num_1))
num_2 = input('Введите второе шестнадцатиричное число: ')
num_list_2 = list(reversed(num_2))
n = 0

min_len = min(len(num_list_1), len(num_list_2))
for i in range(min_len):
    res = hex_to_dec[num_list_1[i]] + hex_to_dec[num_list_2[i]] + n
    n = 0
    if res < 16:
        new_list.append(dec_to_hex[res])
    else:
        n += 1
        new_list.append(dec_to_hex[res - 16])

for j in range(abs(len(num_list_1) - len(num_list_2))):
    if len(num_list_1) > len(num_list_2):
        if hex_to_dec[num_list_1[min_len + j]] + n > 15:
            new_list.append('0')
        else:
            new_list.append(dec_to_hex[hex_to_dec[num_list_1[min_len + j]] + n])
            n = 0
    else:
        if hex_to_dec[num_list_2[min_len + j]] + n > 15:
            new_list.append('0')
        else:
            new_list.append(dec_to_hex[hex_to_dec[num_list_2[min_len + j]] + n])
            n = 0

if n > 0:
    new_list.append(n)

print(list(reversed(new_list)))