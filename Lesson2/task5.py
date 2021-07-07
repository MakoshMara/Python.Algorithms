n = 32  # начало диапазона
m = 128  # конец диапазона
k = 10  # длинна строки
for i in range(n, m):
    print(f' {i} - {chr(i)}', end='')
    if (i - (n - 1)) % k == 0:
        print('')
