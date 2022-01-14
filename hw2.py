import random

number_zxc = 0
x = random.randint(1, 100)
try_count = 0


while True:
    try_count += 1
    number_zxc = int(input('Загадано число от 1 до 100, попытайтесь отгадать это число.Введите число:'))
    if number_zxc == x:
        print(f'Ух ты, {x}! Ты угадал. с  {try_count} попытки')
        if input('сыграем еще?"y|n":') == 'y':
            try_count = 0
            random.randint(1, 100)
        else:
            break
    elif number_zxc > x:
        print('Загаданное число меньше, попробуйте еще')
    else:
        print('Загаданное число больше, попробуйте еще')


# l = [1, 2, 3]
#
# l1= [i * 2 for i in l]
# print(l1)

# l3 = [1, 2, 3]
# res = 0
# for i in l3:
#     res += i ** 2
# print(res)

# l1 = [3, 6.7, 11.8]
# for i in l1:
#     print(int(i*0.5))

# s = 'helloworld'
# if ' ' in s:
#     print(s.upper())
# else:
#     print(s.lower())

# def add_ball(arr):
#     return arr.index('odd') in arr
#
#
#
# print(add_ball(['even', 4, 'even', 7, 'even', 10, 'even', 6, 'even', 11, 'odd', 3, 'even']))
# print(add_ball(['odd', 4, 'even', 7, 'even', 10, 'even', 6, 'even', 9, 'odd', 3, 10]))
# print(add_ball(['even', 4, 'odd', 2]))
#

# def find_sum(n):
#     return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)
#
#
#
# print(find_sum(5))
# print(find_sum(10))


# def mm(names):
#     return [name for name in names if len(name) ==4]
#
# print(mm(['Ryan', 'Kieran', 'Mark', 'John', 'David','Paul']))



# x = random.randint(1, 100)
#
# cnt = 0
# while True:
#     user_num = int(input('загадал число от 1 до 100. попробуй отгадать'))
#     cnt += 1
#     if user_num == x:
#         print(f'ты угадал за {cnt} попыток. спасибо за игру')
#         if input('сыграем еще? "y|n":') == 'y':
#             x = random.randint(1, 100)
#             cnt = 0
#         else:
#             print('спасибо за игру')
#             break
#     elif user_num > x:
#         print('мое число меньше')
#     else:
#         print('Мое число больше')
#
