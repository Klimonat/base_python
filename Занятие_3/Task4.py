def my_func (x, y):
    res = 1
    while y != 0:
        res = res * x
        y += 1
    return 1 / res

num_1 = -1
num_2 = 1
while num_1 <= 0:
    print('Введите действительное положительное число:')
    num_1 = float(input())
while num_2 > 0:
    print('Введите целое отрицательное число:')
    num_2 = int(input())

print("%.2f" % my_func(num_1, num_2))