from typing import TypedDict
from typing import List, Union, Any

# пустая функция, ничего не возвращает

def tickets():
    print("sold out")

'''
Написать функцию, которая принимает число,
возвращает его значение умноженное на два.
'''

def buy_tickets(price) -> Union [int, float]:
    summa: float = price * 2
    return summa
price: float = float(input("Цена билета: "))
print ("Итого за два билета: " + str(buy_tickets(price)))

'''
Напишем функцию, которая определяет параметр на чётность. Если чётное число
принтим (‘yes’) в ином случае ('no')
'''

def check_even(number) -> int:
    if number % 2 ==0:
        print(number, str('это четное число'))
    else:
        print(number, str('это нечетное число'))
number = int(input('введите число: '))
print(check_even(number))


# функция, принимающая два аргумента. проверим, если первое число больше 10 , принтим 'да'). Если меньше('нет')


def check_number(x: Union[int, float], y:Union[int, float]) -> Union[int, float]:
    if x>10:
        print('да')
    else:
        print('нет')

num = check_number(100, 10)
print(num)


# Написать лямбда функцию, которая делит по модулю(%) два аргумента.

print((lambda a, b, type=Union[int,float]: a % b)(22.2, 7))


# map

def title_cities(x):
    return x.title()

l: list = ['london', 'paris', 'milan']
new_list: list = list(map(title_cities, l))
print(new_list)


# функция с декоратором, который бы дополнял возможности функции.

def simple_func(wow):

    def wrapper():
        print('Это подарок, в котором')
        wow()
        print('с днем рождения!')
    return wrapper()

@simple_func
def wow():
    presents: list = ['блокнот', 'наклейки', 'шоколадки']
    money: int = 400
    print(*presents, 'и', money, '$')


# Сделать функцию поиска минимума и максимума в списке.

def find_min_max():
    list1: list = [13, 4, 7, 173, 777, 25]
    max_number: int = max(list1)
    min_number: int = min(list1)
    return max_number, min_number

print(*find_min_max())

'''
Написать функцию, которая определяет, является ли год високосным. Пользователь
вводит год, если он високосный, то функция возвращает True. Если нет, то False
'''

def check_year(year: int):
    if year % 4 == 0 and year % 100 !=0 or year %400 == 0:
        return True
    else:
        return False
year: int = int(input('Введите год: '))
print(check_year(year))

'''
Написать функцию season , принимающую 1 аргумент номер месяца (от 1 до 12), и
возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
'''

def season (month: int):
    if month == 12 or month < 3:
        return 'Зима'
    elif month == 3 or month < 6:
        return 'Весна'
    elif month == 6 or month < 9:
        return 'Лето'
    elif month == 9 or month < 12:
        return 'Осень'
    else:
        return 'Неверно введён номер месяца!'
month: int = int(input('Номер месяца: '))
print(season(month))

'''
Написать функцию date , принимающую 3 аргумента день, месяц и год. Вернуть True, если такая дата есть 
в нашем календаре, и False иначе.
'''

def date(day: int, month: int, year: int) -> bool:
    day = int(input('Day: '))
    month = int(input('Month: '))
    year = int(input('Year: '))
    if day <= 0 or month <= 0 or year < 0:
       return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0:
            months[1] = 29
        if day <= months[month - 1]:
            if month <= 12:
                return True
        return False
print(date('day', 'month', 'year'))

'''
Список [16, 17, 2, 78.7, False , False , {'True': True}, 555, 12, 23, 42, 'DD'] Функция принимает 
на вход список выбирает из него все int и float. составить из него новый
список, отсортированный от наименьшего значения большему.
'''

def create_list():
    list1: list = [16, 17, 2, 78.7, False , False , {'True': True}, 555, 12, 23, 42, 'DD']
    new_list = []
    for i in list1:
        if type(i) == int or type(i) == float:
            new_list.append(i)
            new_list.sort()
    print(new_list)
a = create_list()
print(a)