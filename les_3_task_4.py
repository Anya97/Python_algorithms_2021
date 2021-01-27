"""4. Определить, какое число в массиве встречается чаще всего."""

import random

first_lst = [random.randint(0, 100) for i in range(0, 10)]

number = first_lst[0]

cnt_max = 1
for i in range(len(first_lst) - 1):
    cnt = 1
    for j in range(i + 1, len(first_lst)):
        if first_lst[i] == first_lst[j]:
            cnt += 1
        if cnt > cnt_max:
            cnt_max = cnt
            number = first_lst[i]
if cnt_max > 1:
    print(f'Чаще всего в массиве встречается число: {number}')
else:
    print(f'Все элементы встречаются один раз')


