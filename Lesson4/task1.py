# Для анализа была взята задача №4 из домашней работы к уроку №2:
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
import sys
import cProfile
import timeit

# Вариант 1 (через рекурсию).
sys.setrecursionlimit(5000)


def func_rec(n, b=1):
    if n != 1:
        res = b + func_rec((n - 1), b / (-2))
        return res
    else:
        return b


print(timeit.timeit('func_rec(20)', number=100, globals=globals()))  # 0.0005158000000000003
print(timeit.timeit('func_rec(40)', number=100, globals=globals()))  # 0.000993800000000003
print(timeit.timeit('func_rec(80)', number=100, globals=globals()))  # 0.002013000000000001
print(timeit.timeit('func_rec(160)', number=100, globals=globals()))  # 0.004195499999999998
print(timeit.timeit('func_rec(320)', number=100, globals=globals()))  # 0.010605100000000006

cProfile.run('func_rec(1000)')
# 1003 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1000/1    0.001    0.000    0.001    0.001 task1.py:9(func_rec)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('func_rec(2000)')
#    2000/1    0.002    0.000    0.002    0.002 task1.py:9(func_rec)
cProfile.run('func_rec(4000)')


#    4000/1    0.005    0.000    0.005    0.005 task1.py:9(func_rec)


# Вариант 2 (через цикл).
def func_loop(n):
    i = 1
    s = 0
    for k in range(n):
        s += i
        i /= -2
    return s


print('****************************')
print(timeit.timeit('func_loop(20)', number=100, globals=globals()))  # 0.0002334000000000086
print(timeit.timeit('func_loop(40)', number=100, globals=globals()))  # 0.0004134999999999972
print(timeit.timeit('func_loop(80)', number=100, globals=globals()))  # 0.000777899999999998
print(timeit.timeit('func_loop(160)', number=100, globals=globals()))  # 0.0015142999999999962
print(timeit.timeit('func_loop(320)', number=100, globals=globals()))  # 0.0032805999999999946

cProfile.run('func_loop(10000)')
# 4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task1.py:37(func_loop)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('func_loop(100000)')
#         1    0.013    0.013    0.013    0.013 task1.py:37(func_loop)
cProfile.run('func_loop(1000000)')


#         1    0.137    0.137    0.137    0.137 task1.py:37(func_loop)

# Вариант 3 (в обход огарничения на встроенные функции и списки).
def func_another(n, b=1):
    r = [b]
    while len(r) < n:
        r.append(b / (-2))
        b = b / (-2)
    return sum(r)


print('****************************')
print(timeit.timeit('func_another(20)', number=100, globals=globals()))  # 0.0005958000000000074
print(timeit.timeit('func_another(40)', number=100, globals=globals()))  # 0.0010399999999999854
print(timeit.timeit('func_another(80)', number=100, globals=globals()))  # 0.0020223000000000046
print(timeit.timeit('func_another(160)', number=100, globals=globals()))  # 0.004759799999999981
print(timeit.timeit('func_another(320)', number=100, globals=globals()))  # 0.00881659999999998

cProfile.run('func_another(10000)')
# 20004 function calls in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#         1    0.006    0.006    0.009    0.009 task1.py:67(func_another)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#     10000    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#      9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_another(100000)')

#         1    0.047    0.047    0.073    0.073 task1.py:67(func_another)

cProfile.run('func_another(1000000)')


#         1    0.502    0.502    0.806    0.806 task1.py:67(func_another)

# Вариант 4 (почти как третий, но чтоб был алгоритм с двумя циклами).
def func_another2(n, b=1):
    r = [1]
    s = 0
    if n == 1:
        return s == b
    else:
        while len(r) < n:
            r.append(b / (-2))
            b = b / (-2)
            s = 0
            for j in r:
                s += j
    return s


print('****************************')
print(timeit.timeit('func_another2(20)', number=100, globals=globals()))  # 0.002521399999999785
print(timeit.timeit('func_another2(40)', number=100, globals=globals()))  # 0.006285799999999897
print(timeit.timeit('func_another2(80)', number=100, globals=globals()))  # 0.020890899999999935
print(timeit.timeit('func_another2(160)', number=100, globals=globals()))  # 0.057854300000000025
print(timeit.timeit('func_another2(320)', number=100, globals=globals()))  # 0.2336971000000001

cProfile.run('func_another2(100)')
# 203 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:126(func_another2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('func_another2(1000)')

#         1    0.019    0.019    0.020    0.020 task1.py:126(func_another2)

cProfile.run('func_another2(10000)')
#         1    2.184    2.184    2.188    2.188 task1.py:126(func_another2)
# Первые три алгоритма получились линейной сложности (О(n)). Однако, судя по времени выполнения второй вариант алгоритма самый быстрый (где-то в 2 раза быстрее).
# Третий вариант алгоритма придумывался изначально как самый неэффективный (и он неэффективен, по времени занимает так же как рекурсия),
# однако был (не при помощи зала) добавлен последний четвертый алгоритм для иллюстрации O(n**2). Вот он в итоге занял первую строчку в антирейтинге.
# Даже пришлось на два порядка тестовые данные снижать (по сравлению с алгоритмами №2 и №3) для cProfile иначе падало.
