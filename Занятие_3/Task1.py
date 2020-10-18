def degree(num_1, num_2):
    return num_1 / num_2

print('Введите первое число:')
num_1 = int(input())
print('Введите второе число:')
num_2 = int(input())
while num_2 == 0:
    print('Второе число должно быть отлично от нуля. Введите второе число:')
    num_2 = int(input())

print( "%.3f" % degree(num_1, num_2))
