# пустая функция, ничего не возвращает

def tickets():
    print("sold out")

'''
Написать функцию, которая принимает число,
возвращает его значение умноженное на два.
'''

def buy_tickets():
    price = int(input("Цена билета: "))
    summa = price * 2
    return summa

print ("Итого за два билета: " + str(buy_tickets()))

'''
Напишем функцию, которая определяет параметр на чётность. Если чётное число
принтим (‘yes’) в ином случае ('no')
'''

def check_even ():
    number = int(input('введите число: '))
    if number % 2 ==0:
        print(number, str('это четное число'))
    else:
        print(number, str('это нечетное число'))

print(check_even())


# функция, принимающая два аргумента. проверим, если первое число больше 10 , принтим 'да'). Если меньше('нет')


def check_number(x, y):
    if x>10:
        print('да')
    else:
        print('нет')

num = check_number(100, 10)
print(num)


# Написать лямбда функцию, которая делит по модулю(%) два аргумента.

print((lambda a, b: a % b)(20, 7))


# map

def title_cities(cities):
    return cities.title()

l= ['london, paris, milan']
new_list = list(map(title_cities, l))
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
    presents = ['блокнот', 'наклейки', 'шоколадки']
    money = 400
    print(*presents, 'и', money, '$')


# Сделать функцию поиска минимума и максимума в списке.

def find_min_max():
    list1 = [13, 4, 7, 173, 777, 25]
    max_number = max(list1)
    min_number = min(list1)
    return max_number, min_number

print(*find_min_max())

'''
Написать функцию, которая определяет, является ли год високосным. Пользователь
вводит год, если он високосный, то функция возвращает True. Если нет, то False
'''

def check_year():
    year = int(input('Введите год: '))
    if year % 4 == 0 and year % 100 !=0 or year %400 == 0:
        return True
    else:
        return False

print(check_year())

'''
Написать функцию season , принимающую 1 аргумент номер месяца (от 1 до 12), и
возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
'''

def season ():
    month = int(input('Номер месяца: '))
    if month == 12 or month < 3:
        return 'Зима'
    elif month == 3 or month < 6:
        print ('Весна')
    elif month == 6 or month < 9:
        print ('Лето')
    elif month == 9 or month < 12:
        print('Осень')
    else:
        print('Неверно введён номер месяца!')

print(season())

'''
Написать функцию date , принимающую 3 аргумента день, месяц и год. Вернуть True, если такая дата есть 
в нашем календаре, и False иначе.
'''

def date(day, month, year):
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
    list = [16, 17, 2, 78.7, False , False , {'True': True}, 555, 12, 23, 42, 'DD']
    new_list = []
    for i in list:
        if list[i] == int or float:
            new_list.append(list[i])
            new_list.sort()
            print(new_list)

print(create_list())