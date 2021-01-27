"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

first_lst = [random.randint(0, 333) for i in range(0, 10)]
print(first_lst)

maximum = first_lst[0]
minimum = first_lst[0]
min_index = 0
max_index = 0

for i in range(len(first_lst)):
    if first_lst[i] > maximum:
        maximum = first_lst[i]
        max_index = i
    elif first_lst[i] < minimum:
        minimum = first_lst[i]
        min_index = i
first_lst[max_index], first_lst[min_index] = first_lst[min_index], first_lst[max_index]

print(first_lst)


