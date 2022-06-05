'''
Написать функцию, которая определяет,
является ли год високосным. Пользователь
вводит год, если он високосный, то функция
возвращает True . Если нет, то False
'''

def check_year():
    year = int(input('Введите год: '))
    if year % 4 == 0 and year % 100 !=0 or year %400 == 0:
        return True
    else:
        return False

print(check_year())