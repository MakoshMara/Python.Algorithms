def func(n, b=1):
    if n != 1:
        res = b + func((n - 1), b / (-2))
        return res
    else:
        return b


print(func(int(input("Введите количество элементов ряда (натуральное число), которые необходимо проссумировать: "))))
