#num = 3
#num = -5
num = 0

if num >= 0:
    print('число больше либо равно 0')
else:
    print('число отрицательное')


def task_yes_no():
    str_1 = 'test'
    str_2 = 'test1'

    if str_1 in str_2:
        print('Да')
    else:
        print('нет')

task_yes_no()


#num_float = 3.4
#num_float = 0
num_float = -4.5

if num_float > 0:
    print('Число положительное')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

