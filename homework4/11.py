'''
Написать функцию date , принимающую 3
аргумента день, месяц и год. Вернуть True ,
если такая дата есть в нашем календаре, и
False иначе.*

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