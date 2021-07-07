# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_otr = 0
for i in array:
    if i < 0:
        if max_otr == 0:
            max_otr = i
        if max_otr != 0 and abs(i) < abs(max_otr):
            max_otr = i
print(f'Максимальный отрицательный элемент - {max_otr}, в позиции - {array.index(max_otr)}')
