#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
#Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

def pr_year(k):
    s = k.prq1 + k.prq2 + k.prq3 + k.prq4
    return s

Company = namedtuple('Company', 'name, prq1, prq2, prq3, prq4, pr_year')
count = int(input('Введите количество компаний:'))
k = 0
list_company = [0 for i in range(count)]
while k < count:
    list_company[k] = Company(input('Название:'),
                              int(input('Прибыль Q1:')),
                              int(input('Прибыль Q2:')),
                              int(input('Прибыль Q3:')),
                              int(input('Прибыль Q4:')),pr_year)
    k += 1
s = 0
for i in list_company:
    s = s + i.pr_year(i)
average = s/count
print(f'Средняя прибыль компаний: {average}')

print('Годовая прибыль выше среднего у следующих компаний:')
for i in list_company:
    if i.pr_year(i) > average:
        print(i.name)
print('Годовая прибыль ниже среднего у следующих компаний:')
for i in list_company:
    if i.pr_year(i) < average:
        print(i.name)


