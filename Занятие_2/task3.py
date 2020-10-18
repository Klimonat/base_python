season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', ]
my_dict = {'winter': 'Зима' , 'spring': 'Весна', 'summer': 'Лето', 'autumn': 'Осень' }
print('Введите номер месяца')
number = int(input())
season = season_list [number - 1]
print(my_dict.get(season))
print(month[number - 1])