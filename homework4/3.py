'''
Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае ('no')
'''

def check_even ():
    number = int(input('введите число: '))
    if number % 2 ==0:
        print(number, str('это четное число'))
    else:
        print(number, str('это нечетное число'))

print(check_even())



