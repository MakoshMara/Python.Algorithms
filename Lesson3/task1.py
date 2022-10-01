# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

res = [0 for _ in range(2, 10)]
array = [i for i in range(2, 100)]
for i in array:
    n = 2
    s = 0
    while n < 10:
        if i % n == 0:
            res[s] = res[s] + 1
        n += 1
        s += 1
print(array)
for i, k in enumerate(res, 2):
    print(f'Кратно {i} - {k} элементов')
