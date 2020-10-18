print('Введите результат первого дня')
a = float(input())
print('Введите итоговый результат')
b = float(input())
day = 1

while a < b:
    day = day + 1
    a = a * 1.1

print(day)