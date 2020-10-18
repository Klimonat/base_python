from random import randint
# original_list = [300, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 155]
original_list = [randint(1,1000) for element in range(15)]
final_list = []
i = 1
while i < len(original_list):
    if original_list[i] > original_list[i - 1]:
        final_list.append(original_list[i])
    i += 1
print('Исходный список: ', original_list)
print('Конечный список: ', final_list)
