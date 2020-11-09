# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

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
print(min_, max_)
imax = array.index(max_)
imin = array.index(min_)
array[imin], array[imax] = array[imax], array[imin]
print(array)
