import cProfile
import timeit


def eratosthenes(m):
    a = []
    n = m * 52
    b = [i for i in range(n)]
    b[1] = 0

    for k in range(2, n):
        if b[k] != 0:
            j = k + k
            while j < n:
                b[j] = 0
                j += k
    for item in b:
        if item != 0:
            a.append(item)
    return a[m - 1]


print(timeit.timeit('eratosthenes(100)', number=100, globals=globals()))  # 0.3515253
print(timeit.timeit('eratosthenes(200)', number=100, globals=globals()))  # 0.5858300000000001
print(timeit.timeit('eratosthenes(400)', number=100, globals=globals()))  # 1.2145705
print(timeit.timeit('eratosthenes(800)', number=100, globals=globals()))  # 2.4200236000000004
print(timeit.timeit('eratosthenes(1600)', number=100, globals=globals()))  # 5.1837040000000005
print(timeit.timeit('eratosthenes(3200)', number=100, globals=globals()))  # 11.140237500000001
print(timeit.timeit('eratosthenes(6400)', number=100, globals=globals()))  # 23.185642000000005

cProfile.run('eratosthenes(100)')
# 697 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 task2.py:4(eratosthenes)
#         1    0.000    0.000    0.000    0.000 task2.py:7(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       692    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('eratosthenes(200)')
#         1    0.005    0.005    0.006    0.006 task2.py:4(eratosthenes)

cProfile.run('eratosthenes(400)')


#         1    0.010    0.010    0.012    0.012 task2.py:4(eratosthenes)
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.142    0.142 <string>:1(<module>)
#      1    0.130    0.130    0.142    0.142 task2.py:4(eratosthenes)
#      1    0.010    0.010    0.010    0.010 task2.py:7(<listcomp>)
#      1    0.000    0.000    0.142    0.142 {built-in method builtins.exec}
#  14683    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def not_eratosthenes(m):
    a = [2]
    n = m * 3
    while len(a) < m:
        for k in range(3, n):
            for j in a:
                if k % j == 0:
                    break
            else:
                a.append(k)
        n = n * 2

    return a[m - 1]


print('****************')

print(timeit.timeit('not_eratosthenes(100)', number=100, globals=globals()))  # 0.054580700000000704
print(timeit.timeit('not_eratosthenes(200)', number=100, globals=globals()))  # 0.6646128999999998
print(timeit.timeit('not_eratosthenes(400)', number=100, globals=globals()))  # 2.325157599999999
print(timeit.timeit('not_eratosthenes(800)', number=100, globals=globals()))  # 8.0914781
print(timeit.timeit('not_eratosthenes(1600)', number=100, globals=globals()))  # 27.5793446

cProfile.run('not_eratosthenes(100)')
# 115 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task2.py:56(not_eratosthenes)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       108    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('not_eratosthenes(200)')

#         1    0.006    0.006    0.006    0.006 task2.py:56(not_eratosthenes)

cProfile.run('not_eratosthenes(400)')

#      1    0.021    0.021    0.021    0.021 task2.py:56(not_eratosthenes)


# Выводы: Решето Эратосфена притворяется алгоритмом сложности O(n). Не знаю как так получилось. в википедии по другому написано.
# Сложность второго алгоритма похожа на O(n**2)
# из анализа cProfile могу только сказать, что использование встроенных функций языка не сильно влияет на время выполнения.
# Основная прибавка ко времени выполнения за счет работы самим алгоритмов.
