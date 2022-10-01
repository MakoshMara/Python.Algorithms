#Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

num_1 = deque((input('Введите первое шестнадцатиричное число:')).upper())
num_2 = deque((input('Введите второе шестнадцатиричное число:')).upper())
hex_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
if len(num_2) > len(num_1):
    num_1,num_2 = num_2,num_1
num_1 = num_1[::-1]
num_2 = num_2[::-1]
res = deque()
n = 0
k = 0
for i in num_1:
    first = hex_list.index(i)
    if n > len(num_2) - 1:
        sec = 0 + k
    else:
        sec = hex_list.index(num_2[n]) + k
    res_tek = first + sec
    if res_tek > 15:
        k = 1
        res_tek = res_tek - 16
    else:
        k = 0
    res.appendleft(hex_list[res_tek])
    n += 1

print(f'Результат сложения: {"".join(res)}')
