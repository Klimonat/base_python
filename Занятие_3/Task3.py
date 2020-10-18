def my_func (var_1, var_2, var_3):
    if var_1 < var_2 and var_1 < var_3:
        return var_2 + var_3
    elif var_2 < var_1 and var_2 < var_3:
        return var_1 + var_3
    else:
        return var_1 + var_2

print('Введите первое число:')
num_1 = float(input())
print('Введите второе число:')
num_2 = float(input())
print('Введите третье число:')
num_3 = float(input())

print(my_func(num_1, num_2, num_3))

