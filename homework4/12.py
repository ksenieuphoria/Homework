'''
Список [16, 17, 2, 78.7, False , False , True ’:
True }, 555, 12, 23, 42, ‘DD’] Функция,
принимает на вход список выбирает из него
все int и float составить из него новый
список, отсортированный от наименьшего
значения большему.

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