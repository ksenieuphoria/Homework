'''
Написать функцию, которая принимает число,
возвращает его значение умноженное на два.
'''

def buy_tickets():
    price = int(input("Цена билета: "))
    summa = price * 2
    return summa

print ("Итого за два билета: " + str(buy_tickets()))
