with open("text_1.txt", 'a') as file_obj:
    input_string = input()
    while input_string != '':
        print(input_string, file = file_obj)
        input_string = input()
