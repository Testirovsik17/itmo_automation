def task_1():
    a : int = 1
    b : float = 2,5
    c : str = "test"
    d : list = [1,2,3, "четыре"]
    e : bool = True

    print('тип a ', type(a))
    print('тип b ', type(b))
    print('тип c ', type(c))
    print('тип d ', type(d))
    print('тип e ', type(e))

task_1()


def task_2():
    mylist : list = [1, 2, 3, 5, 8, 13, 21] #ряд фибоначчи
    print(mylist[0:3])

task_2()

def task_3(a : int) -> int:
    return a * a
print(task_3(5))
