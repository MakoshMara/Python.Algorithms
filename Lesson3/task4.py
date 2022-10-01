# Определить, какое число в массиве встречается чаще всего
import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_count = 0
max_count_element = array[0]
max_count_element2 = 0
for i in range(len(array) - 1):
    max_count_i = 1
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            max_count_i += 1
        if max_count_i > max_count:
            max_count = max_count_i
            max_count_element = array[i]

if max_count == 1:
    print(f'Все числа уникальны')
print(f'Чаще всего встречается число {max_count_element}, оно встречается {max_count} раз(а)')
