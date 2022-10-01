def summ(n):
    if n > 1:
        res1 = n + summ(n - 1)
        return res1
    else:
        res1 = n
        return res1


n = int(input('Введите натуральное число (не больше 998, а то рекурсия упадет:)):'))
res1 = summ(n)
res2 = (n * (n + 1)) / 2
if res1 == res2:
    print('Доказано!')
else:
    print('Фигня случилась')
