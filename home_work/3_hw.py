#2
def max_of(a, b):
    print(max(a, b))
max_of(3, 7)


#3
def yes_no(a, b):
    if a - b == 135:
        print("yes")
    elif b - a == 135:
        print("yes")
    else:
        print("no")
yes_no(100, 235)


#4
def season(a: int):
    if a == 12 or a == 1 or a == 2:
        print("зима")
    elif a >= 3 and a <= 5:
        print("весна")
    elif a >= 6 and a <= 8:
        print("лето")
    elif a >= 9 and a <= 11:
        print("осень")
    else:
        print("не корректный ввод")
season(0)


#5
def compare_10(a: int, b: int, c: int):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")
compare_10(12, 15, 30)
compare_10(12, 10, 30)


#6
def list_5(a: list):
    i: int = 0
    for item in a:
        if item > 0:
            i = i + 1
    print("Положительных чисел: ", i)
list_5([0, -3, 2, 0, 0])


#7
def days(a: int, b: int):
    c = a * 12 * 29 + b * 29
    print("дни ", c)
days(1, 1)




