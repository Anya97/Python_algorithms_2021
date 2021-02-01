"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и
возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов. Первый — с помощью алгоритма «Решето Эратосфена»."""

import timeit
from cProfile import run

CONST_RESHETO_SIZE = 2000

def resheto(n):
    a = list(range(n+1))
    a[1] = 0
    b = []
    i = 2
    while i <= n:
        if a[i] != 0:
            b.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return b

def sieve(m):
    c = resheto(CONST_RESHETO_SIZE)
    return c[m - 1]

#num = int(input('Введите номер простого числа: '))
#print(sieve(num))


print(timeit.timeit('resheto(10)', number=1000, globals=globals())) # 0.02049706300000001
print(timeit.timeit('resheto(100)', number=1000, globals=globals())) # 0.12585878500000003
print(timeit.timeit('resheto(1000)', number=1000, globals=globals())) # 1.927986794
print(timeit.timeit('resheto(10_000)', number=1000, globals=globals())) # 13.415730852000001
print(timeit.timeit('resheto(100_000)', number=1000, globals=globals())) # 123.37591234799999


run('resheto(10)')
run('resheto(100)')
run('resheto(1000)')
run('resheto(10_000)')
run('resheto(100_000)')

#         9596 function calls in 0.140 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.003    0.003    0.140    0.140 <string>:1(<module>)
#        1    0.133    0.133    0.137    0.137 les_4_task_2_1.py:11(resheto)
#        1    0.001    0.001    0.140    0.140 {built-in method builtins.exec}
#     9592    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По результатам видно, что время растет как n^2 (сложность алгоритма О(n^2))
