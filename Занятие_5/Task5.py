from random import randint

with open("text_5.txt", 'a', encoding='utf-8') as file_obj:
    str_num = ''
    num = ''
    for count in range(10):
        num = randint(0,100)
        str_num += ' ' + str(num)
    print(str_num, file=file_obj)

with open("text_5.txt", 'r', encoding='utf-8') as file_obj:
    sum_num = 0
    for line in file_obj:
        for number in line.split():
            sum_num += int(number)
        print("Строка: ", line)
    print("Сумма чисел = ", sum_num)
