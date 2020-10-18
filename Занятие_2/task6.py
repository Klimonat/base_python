print('Сколько товаров Вы хотите ввести?')
count = int(input())
i = 1
product = []
list_name = []
list_price = []
list_num = []
list_units = []
while i <= count:
    print('Введите название товара')
    name = input()
    print('Введите стоимость товара')
    price = int(input())
    print('Введите количество товара')
    num = int(input())
    print('Введите единицы товара')
    units = input()
    dict = {'Название': name, 'Стоимость': price, 'Количество': num, 'Единицы': units}
    cort = (i, dict)
    product.append(cort)
    i += 1
print('Структура:', product)

j = 0
while j <= count - 1:
    list_name.append(product[j][1]['Название'])
    list_price.append(product[j][1]['Стоимость'])
    list_num.append(product[j][1]['Количество'])
    list_units.append(product[j][1]['Единицы'])
    j += 1
prop = {'Название': list_name, 'Стоимость': list_price, 'Количество': list_num, 'Единицы': list_units}
print('Аналитика:', prop)