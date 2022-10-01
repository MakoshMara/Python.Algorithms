# Ссылка на диаграммы https://drive.google.com/file/d/1B1yg91YDLf3EcZxZNVXd3Yk4TEjLpmQ7/view?usp=sharing

p = int(input("Введите целое трехзначное число: "))
a = p // 100
b = (p - a * 100) // 10
c = p - a * 100 - b * 10
print(f'Сумма цифр числа: {a + b + c}')
print(f'Произведение цифр числа: {a * b * c}')
