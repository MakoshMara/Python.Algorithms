from collections import Counter
from heapq import heappush, heappop


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'значение {self.value}  левое {self.left} правое {self.right} '

    def sea(self, str_, path=''):
        if str_ != self.value and self.left is not None and self.right is not None:
            self.left.sea(str_, path=path + '0')
            self.right.sea(str_, path=path + '1')
        if str_ == self.value:
            dict_code[self.value] = path



def creating_a_dictionary(s, dict_code):
    if len(s) == 1:
        dict_code[s] = '1'
        return dict_code
    if len(s) == 0:
        dict_code[s] = '0'
        return dict_code
    s_count = Counter(s)
    h = []
    for i, j in s_count.items():
        heappush(h, (j, len(h), MyNode(i)))
    count = len(h)
    while len(h) > 1:
        f1, c1, left = heappop(h)
        f2, c2, right = heappop(h)
        heappush(h, (f1 + f2, count, MyNode(None, left, right)))
        count += 1
    # print(h[0][2]) можно распечататть дерево и убедиться что все в листьях

    for i in s_count:
        dict_code.setdefault(i, h[0][2].sea(i))

    return dict_code

def coding(s, dict_code):
    res = ''
    for i in s:
        res = res + ' ' + dict_code[i]
    return res

s = input('Введите строку для шифрования:')

dict_code = {}
print(f'Словарь для кодирования: {creating_a_dictionary(s,dict_code)}')
print(f'Зашифрованная строка: {coding(s, dict_code)}')
