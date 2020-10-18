def inform(var_1, var_2, var_3, var_4, var_5, var_6):
    return var_1 + ' ' + var_2 + ' ' + var_3 + ' ' + var_4 + ' ' + var_5 + ' ' + var_6

print('Введите имя:')
fname = input()
print('Введите фамилию:')
lname = input()
print('Введите год рождения:')
age = input()
print('Введите город проживания:')
city = input()
print('Введите email:')
mail = input()
print('Введите телефон:')
number = input()

print(inform(var_1=fname, var_3=age, var_2=lname, var_5=mail, var_6=number, var_4=city))