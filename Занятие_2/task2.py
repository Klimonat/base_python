my_list = []
print('Введите первый элемент списка')
my_list.append(input())
print('Введите "1", если хотите ввести новый элемент. Введите "0", если список окончен')
flag = int(input())
while flag == 1:
        print('Введите новый элемент')
        my_list.append(input())
        print('Введите "1", если хотите ввести новый элемент. Введите "0", если список окончен')
        flag = int(input())
if len(my_list) == 1:
    print(my_list)
else:
    count = 0
    while count < 2 * (len(my_list) // 2):
        dop_elem = my_list[count + 1]
        my_list[count + 1] = my_list[count]
        my_list[count] = dop_elem
        count = count + 2
    print(my_list)
