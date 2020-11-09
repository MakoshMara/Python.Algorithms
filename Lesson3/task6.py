# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
min_ = array[0]
for i in array:
    if i < min_:
        min_ = i
    if i > max_:
        max_ = i
print(max_, min_)
imax = array.index(max_)
imin = array.index(min_)
n = abs(imax - imin) - 1
res = 0
while n > 0:
    if imax > imin:
        res = res + array[imax - n]
    if imax < imin:
        res = res + array[imin - n]
    n -= 1

print(f'Сумма элементов между максимальным и минимальным элементами = {res}')
