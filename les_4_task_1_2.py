import timeit
from cProfile import run

"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

# 2 Вариант

result = {'Чётные': 0, 'Нечётные': 0}

def numeral(num):
    new_num = str(num)
    for i in new_num:
        if int(i) % 2 == 0:
            result['Чётные'] += 1
        else:
            result['Нечётные'] += 1
    return result


print(timeit.timeit('numeral(10)', number=1_000_000, globals=globals())) # 3.960293115
print(timeit.timeit('numeral(200)', number=1_000_000, globals=globals())) # 5.37622753
print(timeit.timeit('numeral(40_889)', number=1_000_000, globals=globals())) # 7.445658129
print(timeit.timeit('numeral(853_535)', number=1_000_000, globals=globals())) # 9.438449581
print(timeit.timeit('numeral(16_034_579)', number=1_000_000, globals=globals())) # 13.406973338000004


run('numeral(10)')
run('numeral(200)')
run('numeral(40_889)')
run('numeral(853_535)')
run('numeral(16_034_579)')


#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:13(numeral)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По результатам видно, что время алгоритма, как и в первом случае, растет линейно, сложность О(n)