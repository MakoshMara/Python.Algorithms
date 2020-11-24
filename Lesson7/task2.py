# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы
import random

res = []

def merge(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge(nums[:mid])
    right = merge(nums[mid:])
    return sort(left, right)

def sort(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print(merge(array))