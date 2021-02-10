# 2). Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

START_NUM = 0
LAST_NUM = 49
RNG = 10
lst = [random.randint(START_NUM, LAST_NUM) for i in range(RNG)]


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_part = array[:middle]
        right_part = array[middle:]
        merge_sort(left_part)
        merge_sort(right_part)
        i = 0
        j = 0
        k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            array[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            array[k] = right_part[j]
            j += 1
            k += 1
    return array


print(f'Исходный массив: {lst}')
print(f'Отсортированный массив: {merge_sort(lst)}')
