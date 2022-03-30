from pprint import pprint

def func1(f):
    with open(f,encoding = 'utf-8') as file:
           for string in file:
            x=string.split('\n')[0]
    return x

with open('data2.txt','w', encoding='utf-8') as file:
    x = func1('2.txt')
    file.write(f'{x}\n')
    file.write('1\n')
with open('data2.txt','a', encoding='utf-8') as file:
    x = func1('2.txt')
    file.write(f'{x}\n')

def func2(f):
    x = []
    with open(f,encoding = 'utf-8') as file:
           for string in file:
            x.append(string.split('\n')[0])
    return x

func2('1.txt')

with open('data2.txt','a', encoding='utf-8') as file:
     x = func2('1.txt')
     for i in range(0,len(x)):
        file.write(f'{x[i]}\n')
     file.write(f'2\n')

def func3(f):
    global a, b
    with open(f, encoding='utf-8') as file:
        a = file.readline().split('\n')[0]
        b = file.readline().split('\n')[0]

func3('1.txt')

with open('data2.txt', 'a', encoding='utf-8') as file:
    file.write(f'{a}\n')
    file.write(f'{b}\n')