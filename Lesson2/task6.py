from random import randint

num = randint(0, 100)
max_count = 10
count = 1
while count <= max_count:
    user_num = int(input('Введите целое число от 0 до 100:'))
    if user_num == num:
        print(f'Вы угадали!. Правильный ответ - {num}')
        break
    elif user_num < num:
        print(f'Неверно!. Вы ввели слишком мало')
    else:
        print(f'Неверно!. Вы ввели слишком много')
    print(f'Осталось {max_count - count} попыток')
    count = count + 1
else:
    print(f'Правильный ответ - {num}')
