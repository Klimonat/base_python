original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходный список: ", original_list)
print([element for element in original_list if original_list.count(element) == 1])