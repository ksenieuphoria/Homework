'''
Создадим функцию с простыми командами.
Обернём её в декоратор , который бы дополнял возможности функции.
Использовать функцию map и filter

'''

def title_cities(cities):
    return cities.title()

l= ['london, paris, milan']
new_list = list(map(title_cities, l))
print(new_list)
