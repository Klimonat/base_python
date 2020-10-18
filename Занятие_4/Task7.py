def fact(n):
    mult = 1
    for i in range(n):
        mult *= (i + 1)
        yield mult

print('Введите число: ')
n = int(input())
for el in fact(n):
    print(el)