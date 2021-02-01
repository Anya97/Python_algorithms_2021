import timeit
from cProfile import run

"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

# 1 Вариант

def numeral(num, odd, even):
    if num > 0:
        r = num % 10
        num = num // 10
        if r % 2 == 0:
            even += 1
        else:
            odd += 1
        return numeral(num, odd, even)
    else:
        return even, odd


# print(timeit.timeit('numeral(10, odd=0, even=0)', number=1_000_000, globals=globals())) # 3.0810991580000002
# print(timeit.timeit('numeral(200, odd=0, even=0)', number= 1_000_000, globals=globals())) # 4.341528481
# print(timeit.timeit('numeral(40_889, odd=0, even=0)', number=1_000_000, globals=globals())) # 5.963797745000001
# print(timeit.timeit('numeral(853_535, odd=0, even=0)', number=1_000_000, globals=globals())) # 7.011470126999999
# print(timeit.timeit('numeral(16_034_579, odd=0, even=0)', number=1_000_000, globals=globals())) # 10.259175011


run('numeral(10, odd=0, even=0)')
run('numeral(200, odd=0, even=0)')
run('numeral(40_889, odd=0, even=0)')
run('numeral(853_535, odd=0, even=0)')
run('numeral(16_034_579, odd=0, even=0)')


#         12 function calls (4 primitive calls) in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      9/1    0.000    0.000    0.000    0.000 les_4_task_1.py:11(numeral)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По результатам видно, что время алгоритма растет линейно, сложность О(n)