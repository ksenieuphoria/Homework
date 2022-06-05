'''
Создадим функцию с простыми командами.
Обернём её в декоратор , который бы
дополнял возможности функции.
'''

def simple_func(wow):

    def wrapper():
        print('Это подарок, в котором')
        wow()
        print('с днем рождения!')
    return wrapper()

@simple_func
def wow():
    presents = ['блокнот', 'наклейки', 'шоколадки']
    money = 400
    print(*presents, 'и', money, '$')

