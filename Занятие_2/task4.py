print('Введите строку')
str = input()
list = str.split()
number = 1
for i in list:
    if len(i) < 10:
        print('Строка', number, ':', i)
    else:
        print('Строка', number, ':', i[:10])
    number += 1