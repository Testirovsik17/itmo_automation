a: int = 5
b: str = 'строка'
с: list = [1, 2]

def indent(s:str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 123))



def strLen(s : str = '') -> int:
    return len(s)

print(strLen('aaa'))

def maxList(a: list, b: list) -> int:
    return max(len(a), len(b))

print(maxList([1,2,3,5,7,8,9], [1,2,3,5,6]))

def listAppend(a:list) -> list :
    a.append('test')
    return a
print(listAppend([1,2,3]))

def listSum(a:list) -> int :
    sum = 0

    for item in a:
        sum = sum + item
    return sum

print(listSum([1,2,3,4]))

