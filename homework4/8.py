'''
Сделать функцию поиска минимума и
максимума в списке.
'''

def find_min_max():
    list1 = [13, 4, 7, 173, 777, 25]
    max_number = max(list1)
    min_number = min(list1)
    return max_number, min_number

print(*find_min_max())

