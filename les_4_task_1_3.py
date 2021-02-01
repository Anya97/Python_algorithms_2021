import timeit
from cProfile import run

"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

# 3 Вариант


def numeral(num, odd, even):
    new_num = str(num)
    for i, c in enumerate(new_num):
        #odd = 0
        if int(c) % 2 == 0:
            even += 1
        for j in new_num[::-1]:
            if int(j)% 2 != 0:
                odd += 1
    return even, odd


print(timeit.timeit('numeral(10, odd=0, even=0)', number=1_000_000, globals=globals())) # 9.730771253
print(timeit.timeit('numeral(200, odd=0, even=0)', number=1_000_000, globals=globals())) # 14.597727015999999
print(timeit.timeit('numeral(40_889, odd=0, even=0)', number=1_000_000, globals=globals())) # 32.370657327
print(timeit.timeit('numeral(853_535, odd=0, even=0)', number=1_000_000, globals=globals())) # 44.527521934
print(timeit.timeit('numeral(16_034_579, odd=0, even=0)', number=1_000_000, globals=globals())) # 72.604235065


run('numeral(10, odd=0, even=0)')
run('numeral(200, odd=0, even=0)')
run('numeral(40_889, odd=0, even=0)')
run('numeral(853_535, odd=0, even=0)')
run('numeral(16_034_579, odd=0, even=0)')


#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:12(numeral)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""По результатам видно, что время данного алгоритма растет линейно, но сложность О(n^2).
Из всех алгоритмов быстрее всего работает вариант 1 с рекурсией.
Второй вариант использует хэш-таблицы, поэтому время выполнения медленнее, чем у первого
Самый медленный- последний вариант, так как его сложность О(n^2). """