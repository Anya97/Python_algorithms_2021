"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Второй — без использования «Решета Эратосфена»."""

import timeit
from cProfile import run

CONST_PRIME_LIST_SIZE = 2000

def is_prime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    else:
        return True


def prime_list(n):
    a = list(range(2, n))
    b = []
    for i in a:
        if is_prime(i):
            b.append(i)
    return b


def sieve(m):
    c = prime_list(CONST_PRIME_LIST_SIZE)
    return c[m - 1]


#num = int(input('Введите номер простого числа: '))
#print(sieve(num))

print(timeit.timeit('prime_list(10)', number=100, globals=globals())) # 0.001650747000000008
print(timeit.timeit('prime_list(100)', number=100, globals=globals())) # 0.052973590000000015
print(timeit.timeit('prime_list(1000)', number=100, globals=globals())) # 1.662334097
print(timeit.timeit('prime_list(10_000)', number=100, globals=globals())) # 162.002367069


run('prime_list(10)')
run('prime_list(100)')
run('prime_list(1000)')
run('prime_list(10_000)')

#         11231 function calls in 1.377 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.377    1.377 <string>:1(<module>)
#     9998    1.354    0.000    1.354    0.000 les_4_task_2_2.py:11(is_prime)
#        1    0.022    0.022    1.377    1.377 les_4_task_2_2.py:19(prime_list)
#        1    0.000    0.000    1.377    1.377 {built-in method builtins.exec}
#     1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По результатам видно, что время растет как n^2 (сложность алгоритма О(n^2))
# Данный алгоритм работает медленнее, чем Решето Эратосфена