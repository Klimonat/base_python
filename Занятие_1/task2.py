print('Введите время в секундах')
time = int(input())
hours = time // 3600
minute = (time - hours * 3600) // 60
second = time - hours * 3600 - minute * 60
print('Время %02.f:%02.f:%02.f' % (hours, minute, second))