"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать."""

import random

first_lst = [random.randint(0, 333) for i in range(0, 10)]


def summa_maximum_minimum(lst):
    maximum = lst[0]
    minimum = lst[0]
    min_index = 0
    max_index = 0
    summa = 0

    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]
            max_index = i
        elif lst[i] < minimum:
            minimum = lst[i]
            min_index = i

    if max_index > min_index:
        for j in lst[min_index + 1:max_index]:
            summa += j
    else:
        for j in lst[max_index + 1:min_index]:
            summa += j
    return summa


print(summa_maximum_minimum(first_lst))
