while True:
    n1 = int(input('Введите число: '))
    n2 = int(input('Введите второе число: '))
    s = input('Что сделать с числом? (+,-,*,/): ') # s in ('+', '-', '*', '/')
    while True:
        if s == '+':
            print('Сумма чисел равна: ' + str(n1 + n2))
            break
        elif s == '-':
            print('Разность чисел равна: ' + str(n1 - n2))
            break
        elif s == '*':
            print('Произведение чисел равно: ' + str(n1 * n2))
            break
        elif s == '/':
            if n2 != 0:
                print('Разность чисел равна: ' + str(n1 / n2))
                break
            else:
                print('Деление на ноль!')
                break
        else:
            print('Неверный знак операции!')
            s = input('Что сделать с числом? (+,-,*,/): ')