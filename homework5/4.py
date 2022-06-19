from typing import List, Union, Any


def dec(f):
    def wrapper():
        print ('степень суммы чисел x, y = ', f() **2)
    return wrapper

@dec
def summ():
    x = int(input('введите число '))
    y = int(input('введите второе число '))
    return x + y

print(summ())