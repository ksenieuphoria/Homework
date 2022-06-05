'''
Написать функцию season , принимающую 1
аргумент номер месяца (от 1 до 12), и
возвращающую время года, которому этот
месяц принадлежит
(зима, весна, лето или осень).
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
