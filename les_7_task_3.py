# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
# части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

# вариант без сортировки

import random

START_NUM = 1
LAST_NUM = 100
RNG = 10
lst = [random.randint(START_NUM, LAST_NUM) for i in range(2 * random.randint(START_NUM, LAST_NUM) + 1)]


def find_median(array):
    for i in range(len(array)):
        a = 0
        b = 0
        for j in range(len(array)):
            if array[i] > array[j]:
                a += 1
            elif array[i] == array[j]:
                a += 1
                b += 1
            else:
                b += 1
        if a == b:
            return array[i]


print(f'Медиана массива: {sorted(lst)[(len(lst) // 2)]}')  # проверка
print(f'Медиана массива: {find_median(lst)}')


# вариант с сортировкой

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(f'Медиана массива: {bubble_sort(lst)[len(lst) // 2]}')
