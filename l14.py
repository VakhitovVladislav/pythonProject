l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
l2 = list('hello')
l3 = list((1, 2, 3))
l4 = [i for i in 'hello']
l5 = [i for i in 'hello world' if i not in [' ','a', 'e', 'i', 'o', 'u']]
l6 = list(range(0,11))
print(l, l2, l3, l4, l5, l6, sep = '\n')


for i in range(1, 3):
    print(f'Внешний цикл №{i}')
    for j in range(1, 3):
        print(f'\tВнутренний цикл №{j}')