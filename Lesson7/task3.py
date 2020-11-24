# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы
import random

m = 5
SIZE = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив - {array}')

mid = int(2 * m / 2)
left = array[:mid]
right = array[mid + 1:]

for i in range(len(left)):
    for j in range(len(right)):
        if left[i] > right[j]:
            left[i], right[j] = right[j], left[i]
middle = array[mid]
for i in range(len(left)):
    if left[i] > middle:
        middle, left[i] = left[i], middle
for j in range(len(right)):
    if right[j] < middle:
        middle, right[j] = right[j], middle
middle = [middle]
print(f'Медиана - {middle}')
res = left + middle + right
print(f'Результат - {res}')

# Проверка верности медианы пузырьком из task1
def bubble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array
print(bubble(array)[mid])