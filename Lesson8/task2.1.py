from collections import Counter, deque
from operator import attrgetter


class MyNode:
    def __init__(self, value, w=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.w = w

    def __str__(self):
        return f'значение {self.value} вес {self.w} левое {self.left} правое {self.right} '

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
    b = []
    for i, j in s_count.items():
        b.append(MyNode(i, j))
    b = deque(sorted(b, key=attrgetter('w')))
    if len(b) % 2 != 0:
        z = b.popleft()
    else:
        z = None
    while len(b) > 1:
        left = b.pop()
        right = b.pop()
        b.appendleft(MyNode(None, left.w + right.w, left, right))
        if z is not None:
            t = b.popleft()
            if t.w >= z.w:
                b.extendleft([z, t])
            else:
                b.extendleft([t, z])
            z = None
    # print(b[0]) можно распечататть дерево и убедиться что все в листьях
    for i in s_count:
        dict_code.setdefault(i, b[0].sea(i))

    return dict_code


def coding(s, dict_code):
    res = ''
    for i in s:
        res = res + ' ' + dict_code[i]
    return res


s = input('Введите строку для шифрования:')
dict_code = {}
print(f'Словарь для шифрования: {creating_a_dictionary(s, dict_code)}')
print(f'Закодированная строка: {coding(s, dict_code)}')
