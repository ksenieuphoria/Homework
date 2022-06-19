from typing import List

list1: list = [16, 17, 2, 78.7, False , False , {'True': True}, 555, 12, 23, 42, 'DD']

def create_list():
    for i in list1:
        yield i

a = create_list()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))